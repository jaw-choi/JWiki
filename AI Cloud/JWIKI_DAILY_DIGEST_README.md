# JWiki 일일 대화 통합 요약

`jwiki_daily_digest.py`는 Codex Desktop의 로컬 세션 로그를 날짜별로 읽어 하나의 JWiki Markdown 노트로 만듭니다. 필요하면 별도 JSONL 기록도 함께 합칠 수 있습니다.

## 1. Codex 대화 자동 수집

Codex Desktop 대화는 기본적으로 `C:\Users\Admin\.codex\sessions\YYYY\MM\DD` 아래의 세션 로그에 저장됩니다. 스크립트는 실행 당일의 사용자·도우미 메시지만 읽으며, 시스템 지시·도구 호출은 요약 대상에서 제외합니다.

## 2. 추가 대화 로그 형식

`C:\JWiki\AI Cloud\conversation-logs` 아래에 `.jsonl` 파일을 둡니다. 한 줄이 메시지 하나입니다.

```json
{"timestamp":"2026-09-09T09:00:00+09:00","conversation_id":"codex-wallpaper","role":"user","content":"파일 정보를 정리해줘"}
{"timestamp":"2026-09-09T09:01:00+09:00","conversation_id":"codex-wallpaper","role":"assistant","content":"표를 만들었습니다."}
```

여러 대화는 `conversation_id`를 다르게 하거나 파일을 분리하면 됩니다. 스크립트는 해당 날짜의 모든 JSONL 기록을 합칩니다.

## 3. API 키 설정

PowerShell에서 한 번만 실행합니다. 키 값은 따옴표 안에 직접 넣습니다.

```powershell
[Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'YOUR_API_KEY', 'User')
```

새 PowerShell 창을 연 뒤 실행합니다. API 호출에는 별도 비용이 발생할 수 있습니다.

## 4. Gmail 발송 설정

요약이 저장된 뒤 `wod6983@gmail.com`으로 같은 내용을 메일로 보냅니다. Gmail 계정에서 2단계 인증을 활성화하고 **앱 비밀번호**를 만든 뒤, PowerShell에서 아래 환경 변수를 설정합니다. 일반 Gmail 비밀번호는 사용하지 않습니다.

```powershell
[Environment]::SetEnvironmentVariable('GMAIL_ADDRESS', 'wod6983@gmail.com', 'User')
[Environment]::SetEnvironmentVariable('GMAIL_APP_PASSWORD', 'GMAIL_APP_PASSWORD_HERE', 'User')
```

앱 비밀번호는 외부에 공유하거나 Markdown 파일에 적지 마세요. 새 PowerShell 창을 연 뒤 스크립트를 실행합니다.

## 5. 수동 실행과 검증

```powershell
python C:\JWiki\AI Cloud\jwiki_daily_digest.py --date 2026-09-09 --dry-run
python C:\JWiki\AI Cloud\jwiki_daily_digest.py --date 2026-09-09
```

결과는 `C:\JWiki\AI Cloud\YYYY-MM-DD.md`에 저장됩니다. 같은 날짜의 원본 대화가 바뀌면 해당 날짜 노트를 새 통합 요약으로 갱신하며, 바뀌지 않았다면 다시 API를 호출하지 않습니다.

## 6. 매일 오후 6시 실행

검증 후 Windows 작업 스케줄러에서 프로그램 시작 작업을 만듭니다.

- 프로그램: 설치된 Python 실행 파일
- 인수: `"C:\JWiki\AI Cloud\jwiki_daily_digest.py"`
- 시작 위치: `C:\JWiki\AI Cloud`
- 트리거: 매일 오후 6시

## 제한

이 스크립트는 이 PC의 Codex Desktop 로컬 세션 로그를 대상으로 합니다. ChatGPT 웹·모바일 대화는 이 파일에 자동으로 포함되지 않습니다.
