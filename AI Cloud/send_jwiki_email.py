"""Send today's JWiki Markdown note as an email body."""

from __future__ import annotations

import argparse
import os
import smtplib
import ssl
from datetime import datetime
from email.message import EmailMessage
from pathlib import Path
from zoneinfo import ZoneInfo


SEOUL = ZoneInfo("Asia/Seoul")
ROOT = Path(r"C:\JWiki\AI Cloud")
MAIL_TO = "wod6983@gmail.com"


def main() -> None:
    parser = argparse.ArgumentParser(description="Send today's JWiki note through Gmail.")
    parser.add_argument("--dry-run", action="store_true", help="Check the note without sending email.")
    args = parser.parse_args()

    day = datetime.now(SEOUL).date().isoformat()
    note_path = ROOT / f"{day}.md"
    if not note_path.is_file():
        print(f"{day}: 발송할 JWiki 파일이 없습니다.")
        return

    note_content = note_path.read_text(encoding="utf-8").strip()
    if not note_content:
        print(f"{day}: JWiki 파일이 비어 있어 발송하지 않습니다.")
        return

    if args.dry_run:
        print(f"{day}: 발송 대상 파일 확인 완료: {note_path}")
        return

    gmail_address = os.environ.get("GMAIL_ADDRESS")
    gmail_app_password = os.environ.get("GMAIL_APP_PASSWORD")
    if not gmail_address or not gmail_app_password:
        raise RuntimeError("GMAIL_ADDRESS와 GMAIL_APP_PASSWORD 환경 변수를 설정해야 합니다.")

    message = EmailMessage()
    message["Subject"] = f"[JWiki 일일 대화 요약] {day}"
    message["From"] = gmail_address
    message["To"] = MAIL_TO
    message.set_content(note_content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(gmail_address, gmail_app_password)
        server.send_message(message)

    print(f"{day}: JWiki 파일 내용을 메일로 발송했습니다.")


if __name__ == "__main__":
    main()
