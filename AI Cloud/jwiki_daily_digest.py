"""Create a daily JWiki note from exported conversation logs.

Logs are newline-delimited JSON (JSONL). Each record must contain:
timestamp, conversation_id, role, content
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import smtplib
import ssl
import tempfile
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from zoneinfo import ZoneInfo


SEOUL = ZoneInfo("Asia/Seoul")
ROOT = Path(r"C:\JWiki\AI Cloud")
LOG_DIR = ROOT / "conversation-logs"
STATE_DIR = ROOT / ".daily-digest-state"
MAIL_TO = "wod6983@gmail.com"
CODEX_SESSION_DIR = Path.home() / ".codex" / "sessions"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a JWiki daily conversation digest.")
    parser.add_argument("--date", help="Target date in YYYY-MM-DD (default: today in Asia/Seoul).")
    parser.add_argument("--dry-run", action="store_true", help="Do not call the API or write a note.")
    return parser.parse_args()


def target_date(value: str | None) -> str:
    if value is None:
        return datetime.now(SEOUL).date().isoformat()
    return datetime.strptime(value, "%Y-%m-%d").date().isoformat()


def load_exported_records(day: str) -> list[dict]:
    records: list[dict] = []
    for log_file in sorted(LOG_DIR.rglob("*.jsonl")):
        for line_number, raw_line in enumerate(log_file.read_text(encoding="utf-8").splitlines(), start=1):
            if not raw_line.strip():
                continue
            try:
                record = json.loads(raw_line)
                stamp = datetime.fromisoformat(record["timestamp"].replace("Z", "+00:00")).astimezone(SEOUL)
                if stamp.date().isoformat() != day:
                    continue
                if not all(key in record for key in ("conversation_id", "role", "content")):
                    raise ValueError("missing required key")
                record["_timestamp"] = stamp
                record["_source"] = f"{log_file.name}:{line_number}"
                records.append(record)
            except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
                print(f"Skipped invalid record {log_file}:{line_number} ({error})")
    return sorted(records, key=lambda item: item["_timestamp"])


def load_codex_records(day: str) -> list[dict]:
    """Read user and assistant messages from Codex Desktop's local session logs."""
    year, month, date = day.split("-")
    day_directory = CODEX_SESSION_DIR / year / month / date
    records: list[dict] = []
    if not day_directory.is_dir():
        return records

    for session_file in sorted(day_directory.glob("*.jsonl")):
        session_id = session_file.stem
        for line_number, raw_line in enumerate(session_file.read_text(encoding="utf-8").splitlines(), start=1):
            try:
                item = json.loads(raw_line)
                payload = item.get("payload", {})
                if item.get("type") == "session_meta":
                    session_id = payload.get("session_id", session_id)
                    continue
                if item.get("type") != "response_item" or payload.get("type") != "message":
                    continue
                if payload.get("role") not in {"user", "assistant"}:
                    continue
                text = "\n".join(
                    part.get("text", "")
                    for part in payload.get("content", [])
                    if part.get("type") in {"input_text", "output_text"} and part.get("text")
                ).strip()
                if not text:
                    continue
                stamp = datetime.fromisoformat(item["timestamp"].replace("Z", "+00:00")).astimezone(SEOUL)
                records.append({
                    "timestamp": item["timestamp"],
                    "conversation_id": session_id,
                    "role": payload["role"],
                    "content": text,
                    "_timestamp": stamp,
                    "_source": f"{session_file.name}:{line_number}",
                })
            except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
                print(f"Skipped invalid Codex record {session_file}:{line_number} ({error})")
    return records


def load_day_records(day: str) -> list[dict]:
    records = load_exported_records(day) + load_codex_records(day)
    return sorted(records, key=lambda item: item["_timestamp"])


def digest_id(records: list[dict]) -> str:
    normalized = [
        {key: item[key] for key in ("timestamp", "conversation_id", "role", "content")}
        for item in records
    ]
    return hashlib.sha256(json.dumps(normalized, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def transcript(records: list[dict]) -> str:
    grouped: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        grouped[str(record["conversation_id"])].append(record)

    sections = []
    for conversation_id, messages in grouped.items():
        lines = [f"## 대화 {conversation_id}"]
        for message in messages:
            time = message["_timestamp"].strftime("%H:%M")
            lines.append(f"[{time}] {message['role']}: {message['content']}")
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def summarize(source_text: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")

    instructions = """다음은 한 사용자가 하루 동안 나눈 여러 대화의 기록이다.
한국어 Markdown으로 간결하게 정리하라. 반드시 다음 제목을 사용한다:
## 핵심 요약
## 결정 및 완료한 일
## 후속 할 일
사실만 쓰고, 비밀값·인증정보·개인정보로 보이는 내용은 기록하지 마라.
대화별 세부 발화는 그대로 반복하지 마라."""
    body = {
        "model": "gpt-5.6-terra",
        "input": [{"role": "user", "content": [{"type": "input_text", "text": f"{instructions}\n\n{source_text}"}]}],
    }
    request = urllib.request.Request(
        "https://api.openai.com/v1/responses",
        data=json.dumps(body, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"OpenAI API 요청 실패: HTTP {error.code}") from error

    text_parts = []
    for output in payload.get("output", []):
        for content in output.get("content", []):
            if content.get("type") == "output_text":
                text_parts.append(content.get("text", ""))
    result = "\n".join(text_parts).strip()
    if not result:
        raise RuntimeError("OpenAI API 응답에서 요약 텍스트를 찾지 못했습니다.")
    return result


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, dir=path.parent, suffix=".tmp") as handle:
        handle.write(text)
        temporary_path = Path(handle.name)
    temporary_path.replace(path)


def send_email(day: str, summary: str, note_path: Path) -> None:
    """Send the completed digest using Gmail SMTP credentials from environment variables."""
    gmail_address = os.environ.get("GMAIL_ADDRESS")
    gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")
    if not gmail_address or not gmail_app_password:
        raise RuntimeError("GMAIL_ADDRESS와 GMAIL_APP_PASSWORD 환경 변수를 설정해야 메일을 보낼 수 있습니다.")

    message = EmailMessage()
    message["Subject"] = f"[JWiki 일일 대화 요약] {day}"
    message["From"] = gmail_address
    message["To"] = MAIL_TO
    message.set_content(f"# {day}\n\n{summary}\n\n저장 파일: {note_path}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(gmail_address, gmail_app_password)
        server.send_message(message)


def main() -> None:
    args = parse_args()
    day = target_date(args.date)
    records = load_day_records(day)
    if not records:
        print(f"{day}: 기록할 대화가 없습니다.")
        return

    current_digest_id = digest_id(records)
    state_path = STATE_DIR / f"{day}.sha256"
    if state_path.exists() and state_path.read_text(encoding="utf-8").strip() == current_digest_id:
        print(f"{day}: 새 대화가 없어 이미 최신입니다.")
        return

    print(f"{day}: {len(records)}개 메시지, {len(set(item['conversation_id'] for item in records))}개 대화를 발견했습니다.")
    if args.dry_run:
        return

    summary = summarize(transcript(records))
    note_path = ROOT / f"{day}.md"
    note = f"# {day}\n\n{summary}\n"
    atomic_write(note_path, note)
    send_email(day, summary, note_path)
    atomic_write(state_path, current_digest_id + "\n")
    print(f"저장 및 메일 발송 완료: {note_path}")


if __name__ == "__main__":
    main()
