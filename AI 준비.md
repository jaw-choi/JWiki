# 1. 1209 면접 예상 질문 + 답변 예시

## Q1. 왜 이 과정에 지원했나요?

> 기존에 C++과 C#을 활용해 Unity와 Unreal 기반 프로젝트를 진행하면서 소프트웨어 개발 경험을 쌓았습니다. 최근에는 AI가 단순 모델 활용을 넘어 실제 소프트웨어 기능과 결합되는 방향으로 빠르게 발전하고 있다고 생각했습니다. 이 과정은 LLM과 RAG뿐 아니라 AI Agent, Docker, Cloud, MLOps까지 실제 서비스를 만드는 데 필요한 기술을 함께 배울 수 있다는 점이 매력적이었습니다. 기존 개발 경험에 AI 역량을 추가해 AI Software Engineer로 성장하고 싶어 지원했습니다.

**핵심 키워드:**  
`기존 개발경험 → AI 확장 → 실제 서비스 → 취업`

---

## Q2. 왜 AI 분야로 전환하려 하나요?

> 기존 게임과 소프트웨어 개발을 하면서 정해진 로직을 직접 구현해 왔는데, LLM과 AI Agent가 등장하면서 소프트웨어가 사용자의 요청을 이해하고 스스로 도구를 선택해 문제를 해결하는 방향으로 변화하고 있다는 점에 관심을 갖게 됐습니다. 기존 개발 경험을 버리는 전환이라기보다 C++과 C#으로 쌓은 프로그래밍 및 시스템 설계 능력에 Python과 AI 기술을 더하는 확장이라고 생각합니다.

이 답변이 좋습니다.

**“게임개발이 취업 안 돼서 AI로 바꿉니다.”**  
이런 식으로 말하면 안 됩니다.

---

## Q3. 기존 개발경험을 설명해주세요.

> C++, C#을 중심으로 Unity와 Unreal Engine 프로젝트를 진행했습니다. C++ 프로젝트에서는 자료구조와 A* 경로탐색, 공간분할 등을 직접 구현했고, Unreal 팀 프로젝트에서는 AIController, Behavior Tree, Blackboard 등을 이용해 몬스터 AI를 구현했습니다. Unity 프로젝트에서는 게임 시스템과 UI, Firebase 등을 연동한 경험이 있습니다. 팀 프로젝트를 진행하면서 Git과 Perforce를 통한 협업 경험도 쌓았습니다. 이러한 경험을 AI 서비스 개발에도 활용하고 싶습니다.

여기서는 **프로젝트 이름을 여러 개 말하는 것보다 기술적으로 무엇을 했는지** 설명하는 게 중요합니다.

---

## Q4. C++/C#을 했는데 왜 Python/AI인가요?

> 언어 자체를 바꾸는 것이 목표라기보다 문제에 맞는 도구를 확장하는 것이라고 생각합니다. C++과 C#을 통해 객체지향, 자료구조, 알고리즘과 프로그램 구조에 대한 기반을 갖췄고, Python은 AI와 데이터 분야의 생태계가 매우 크기 때문에 추가로 익히려고 합니다. 기존 프로그래밍 기반이 있기 때문에 Python 문법을 익힌 뒤에는 AI 라이브러리와 서비스 구현에 집중할 수 있다고 생각합니다.

**좋은 포인트:**  
“C++ 포기 → Python 전환” ❌  
“C++ 기반 + Python 추가” ⭕

---

## Q5. AI Software Engineer가 어떤 직무라고 생각하나요?

> AI 모델을 연구하는 것에만 집중하기보다 AI 기술을 실제 서비스 안에서 사용할 수 있도록 구현하는 개발자라고 생각합니다. 예를 들어 LLM과 RAG를 이용해 기업 문서를 검색하거나 AI Agent가 외부 API와 데이터베이스를 활용하도록 만들고, 이를 서버와 클라우드 환경에 배포해 사용자에게 안정적으로 제공하는 역할입니다. 그래서 AI뿐 아니라 소프트웨어 설계, API, 데이터베이스, 배포에 대한 이해도 필요하다고 생각합니다.

아주 중요한 질문입니다.

한 문장 버전:

> **AI 기술을 실제 제품과 서비스로 구현하는 소프트웨어 엔지니어라고 생각합니다.**

---

## Q6. LLM과 RAG가 무엇인지 알고 있나요?

> LLM은 대규모 텍스트 데이터를 학습해 자연어를 이해하고 생성하는 모델입니다. 다만 학습 시점 이후의 정보나 특정 회사의 내부 데이터는 알지 못할 수 있고 잘못된 내용을 생성하는 문제도 있습니다. RAG는 사용자의 질문과 관련된 외부 문서를 검색한 뒤 그 내용을 LLM에게 함께 제공해 답변하도록 하는 방식입니다. 이를 통해 최신 정보나 기업 내부 데이터를 활용하고 답변의 근거성을 높일 수 있습니다.

그림으로 기억하면 됩니다.

```
질문
 ↓
Embedding
 ↓
Vector DB 검색
 ↓
관련 문서 검색
 ↓
LLM에 질문 + 문서 제공
 ↓
답변
```

---

## Q7. 팀 프로젝트에서 맡았던 역할은?

당신은 Unreal 경험을 쓰는 게 좋습니다.

> Unreal 팀 프로젝트에서 몬스터 AI 구현을 담당했습니다. AIController, Behavior Tree, Blackboard를 이용해 몬스터의 탐색, 추적, 공격 상태를 구성하고 Animation Montage와 Root Motion 등을 연동했습니다. 개발 과정에서 다른 팀원이 만든 캐릭터 및 전투 시스템과 연결해야 했기 때문에 인터페이스와 데이터 흐름을 맞추는 작업도 필요했습니다. 이 경험을 통해 개인 구현뿐 아니라 다른 시스템과의 연동과 팀 커뮤니케이션이 중요하다는 것을 배웠습니다.

---

## Q8. 문제를 해결했던 경험은?

기술적인 사례 하나를 확실하게 준비하세요.

> Unreal 프로젝트에서 몬스터가 공격 과정에서 정상적으로 동작하지 않는 문제가 있었습니다. 처음에는 애니메이션 문제라고 생각했지만 로그와 실행 흐름을 확인하면서 AI 상태 전환과 객체 참조를 단계별로 추적했습니다. 그 과정에서 특정 상황에서 참조 값이 유효하지 않은 상태로 처리되는 문제를 발견했습니다. 단순히 에러가 발생한 부분만 수정하지 않고 호출 흐름과 상태 전환을 확인해 원인을 찾았고, 이후 유효성 검사와 상태 처리 구조를 수정했습니다. 이 경험을 통해 문제 발생 시 추측보다 로그와 데이터 흐름을 기반으로 원인을 좁히는 습관을 갖게 됐습니다.

**면접관이 좋아할 구조:**

`문제 → 분석 → 원인 → 해결 → 배운 점`

---

## Q9. 6개월 풀타임 교육을 끝까지 할 수 있나요?

> 네. 단순히 AI를 경험해 보는 것이 아니라 수료 후 관련 직무 취업을 목표로 지원했기 때문에 교육기간 동안 학습과 프로젝트에 우선순위를 두고 참여할 계획입니다. 기존에도 프로젝트를 일정에 맞춰 끝까지 진행한 경험이 있으며, 수업 외 시간에는 부족한 부분을 복습하고 GitHub에 학습 내용과 프로젝트 결과를 지속적으로 정리할 계획입니다.

---

## Q10. 수료 후 어떤 회사/직무에 취업하고 싶은가요?

> 특정 회사 하나만 목표로 하기보다는 LLM, RAG, AI Agent를 실제 서비스에 적용하는 기업에서 AI Software Engineer로 시작하는 것이 목표입니다. 특히 기존 소프트웨어 개발 경험을 활용할 수 있는 AI 서비스 기업이나 IT 플랫폼, 게임·콘텐츠 기업의 AI 개발 직무에도 관심이 있습니다. 장기적으로는 AI 서비스를 설계부터 배포와 운영까지 담당할 수 있는 엔지니어로 성장하고 싶습니다.

이게 가장 좋습니다.

**Backend Engineer**를 굳이 목표라고 말하지 않아도 됩니다.

---

# 2. Python 연습 사이트

### 1순위 — Exercism Python

Python 문법 자체를 익히는 데 가장 추천합니다.

Basics → Bool → Numbers → Conditionals 등 개념별 연습과 Practice Exercise가 별도로 있고 무료입니다.

[Exercism Python Track](https://exercism.org/tracks/python?utm_source=chatgpt.com)

### 2순위 — HackerRank Python

레벨테스트 대비에 좋습니다.

Python뿐 아니라 Algorithms, Data Structures, SQL까지 주제별 문제가 있습니다.

[HackerRank Practice](https://www.hackerrank.com/domains/python?utm_source=chatgpt.com)

### 추천 학습법

**Exercism = Python다운 문법 익히기**

**HackerRank = 시험/코딩 문제 대비**

로 사용하세요.

---

# 3. Python 자체 연습문제

## Level 1 — 기본문법

### PY-01 짝수 합

정수 리스트가 주어질 때 짝수의 합을 반환하세요.

```
numbers = [1, 4, 7, 10, 13, 16]
```

예상 결과:

```
30
```

사용:

- `for`
- `if`
- `%`

---

### PY-02 문자열 빈도

다음 리스트에서 각 과일이 몇 번 등장했는지 `dict`로 만드세요.

```
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
```

예상:

```
{
    "apple": 3,
    "banana": 2,
    "orange": 1
}
```

---

### PY-03 List Comprehension

1~20에서 3의 배수만 골라 제곱한 리스트를 한 줄로 작성하세요.

예상:

```
[9, 36, 81, 144, 225, 324]
```

---

### PY-04 함수

다음 함수를 작성하세요.

```
def average(numbers):
    pass
```

조건:

- 리스트 평균 반환
- 빈 리스트면 `0` 반환

---

### PY-05 문자열 처리

입력:

```
"Python AI Engineer"
```

출력:

```
"reenignE IA nohtyP"
```

---

# 4. Python 중급

### PY-06 클래스

다음 조건을 만족하는 `Student` 클래스를 작성하세요.

```
속성
- name
- scores

메서드
- average()
- is_passed()
```

`average >= 60`이면 합격.

---

### PY-07 파일처리

`log.txt`에서 `"ERROR"`가 포함된 줄만 읽어 리스트로 저장하세요.

---

### PY-08 예외처리

사용자에게 두 숫자를 받아 나누는 프로그램을 작성하세요.

처리해야 할 예외:

```
숫자가 아닌 입력
0으로 나누기
```

---

### PY-09 Dictionary + 정렬

다음 데이터를 점수가 높은 순서대로 출력하세요.

```
scores = {
    "Kim": 82,
    "Lee": 95,
    "Park": 73,
    "Choi": 88
}
```

---

### PY-10 OOP

다음 구조를 구현하세요.

```
Animal
 ├─ Dog
 └─ Cat
```

`Animal`:

```
speak()
```

Dog:

```
"Woof"
```

Cat:

```
"Meow"
```

---

# 5. Linux 연습

Linux는 **OverTheWire Bandit**을 가장 추천합니다.

SSH로 실제 Linux 환경에 접속해서 `ls`, `cd`, `cat`, `file`, `find`, `grep` 등을 이용해 단계별 문제를 해결합니다. 초보자를 대상으로 만들어진 과정입니다.

[OverTheWire Bandit](https://overthewire.org/wargames/bandit/?utm_source=chatgpt.com)

**목표: Bandit 0 → 10까지**

10까지만 해도 1209 초반에 상당히 도움됩니다.

## Linux 자체 문제

### Linux-01

현재 디렉터리 위치 확인.

```
?
```

### Linux-02

현재 디렉터리의 숨김 파일까지 출력.

```
?
```

### Linux-03

`project` 디렉터리를 만들고 이동하세요.

### Linux-04

`server.log`에서 `ERROR`가 들어간 줄만 출력하세요.

### Linux-05

현재 실행 중인 Python Process를 찾으세요.

### Linux-06

PID가 `12345`인 프로세스를 종료하세요.

### Linux-07

`run.sh`에 실행권한을 부여하세요.

### Linux-08

현재 폴더 아래에서 `.py`로 끝나는 모든 파일을 찾으세요.

### Linux-09

SSH가 무엇인지 한 문장으로 설명하세요.

### Linux-10

다음의 차이를 설명하세요.

```
process
port
IP
```

---

# 6. Git

Git은 이미 사용해봤으므로 명령어를 외우는 것보다 **branch/merge/rebase 개념**을 정리하세요.

**Learn Git Branching**은 브라우저에서 Git repository를 시각적으로 보면서 commit, branch, merge, rebase 등을 직접 연습할 수 있고 한국어도 지원합니다.

[Learn Git Branching 한국어](https://learngitbranching.js.org/?locale=ko&utm_source=chatgpt.com)

### 목표

`Introduction Sequence` 전부 완료.

## Git 문제

### Git-01

Git과 GitHub의 차이는?

### Git-02

`git add`와 `git commit` 차이는?

### Git-03

Branch를 사용하는 이유는?

### Git-04

Merge Conflict는 언제 발생하는가?

### Git-05

다음 상황에서 필요한 명령어를 쓰세요.

```
main에서 새로운 ai-agent branch 생성
```

### Git-06

```
git pull
```

은 내부적으로 무엇을 수행하는가?

### Git-07

`merge`와 `rebase` 차이를 설명하세요.

**면접 수준에서는 Git-04까지 확실히 알면 충분합니다.**

---

# 7. HTTP / REST API

FastAPI를 하기 전에 이것부터 이해해야 합니다.

## HTTP-01

Client와 Server의 차이를 설명하세요.

## HTTP-02

다음 HTTP Method의 일반적인 목적을 설명하세요.

```
GET
POST
PUT
DELETE
```

## HTTP-03

다음 Status Code 의미를 설명하세요.

```
200
201
400
401
403
404
500
```

## HTTP-04

JSON이 무엇인가요?

## HTTP-05

REST API란 무엇인가요?

## HTTP-06

다음 요청을 설명하세요.

```
GET /users/10
```

## HTTP-07

다음 요청과 GET의 차이는?

```
POST /users
Content-Type: application/json

{
    "name": "Kim"
}
```

---

# 8. Docker

**Docker 공식 Get Started**에 입문 가이드와 약 45분짜리 Workshop이 있습니다.

설치하기 귀찮으면 **Play with Docker**에서 브라우저만으로 Docker를 실습할 수 있습니다.

[Docker Get Started](https://docs.docker.com/get-started/?utm_source=chatgpt.com)  
[Play with Docker](https://training.play-with-docker.com/?utm_source=chatgpt.com)

## Docker 문제

### Docker-01

다음 차이를 설명하세요.

```
Docker Image
Docker Container
```

### Docker-02

Docker를 사용하는 이유 3가지를 쓰세요.

### Docker-03

다음 Dockerfile을 설명하세요.

```
FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
```

### Docker-04

Image를 만드는 명령어:

```
?
```

### Docker-05

Container를 실행하는 명령어:

```
?
```

### Docker-06

Docker Compose는 왜 사용하는가?

### Docker-07

다음 구조를 Docker Compose로 실행하려면 왜 편리할까요?

```
FastAPI
+
PostgreSQL
+
Redis
```

---

# 9. FastAPI

공식 FastAPI 튜토리얼은 단계별로 구성되어 있고 예제 코드를 그대로 실행할 수 있습니다. 첫 단계에서 GET endpoint와 JSON response부터 시작합니다.

[FastAPI 공식 Tutorial](https://fastapi.tiangolo.com/tutorial/?utm_source=chatgpt.com)

## FastAPI-01

다음 서버를 실행하세요.

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello"}
```

---

## FastAPI-02

다음 API를 구현하세요.

```
GET /users/10
```

결과:

```
{
  "user_id": 10
}
```

---

## FastAPI-03

다음을 받는 POST API를 만드세요.

```
{
  "name": "Kim",
  "age": 30
}
```

---

## FastAPI-04

다음 구조를 만들어보세요.

```
POST /ask

질문
 ↓
서버
 ↓
답변
```

아직 LLM은 필요 없습니다.

```
{
  "question": "What is RAG?"
}
```

를 받으면 임시 문자열을 반환하세요.

---

# 10. SQL

1209 후반을 생각하면 이것까지만 미리 하면 충분합니다.

## SQL-01

다음 테이블이 있다고 가정합니다.

```
users

id | name | age
1  | Kim  | 30
2  | Lee  | 25
3  | Park | 35
```

30세 이상 조회:

```
?
```

## SQL-02

나이가 높은 순으로 정렬하세요.

## SQL-03

새 사용자 추가:

```
Choi / 28
```

## SQL-04

Kim의 나이를 31로 수정.

## SQL-05

Lee 삭제.

## SQL-06

`JOIN`을 사용하는 이유를 설명하세요.

---

# 11. AI / ML 기본 질문

이 부분은 면접에서도 나올 수 있습니다.

### AI-01

AI, Machine Learning, Deep Learning 관계를 설명하세요.

### AI-02

Supervised Learning과 Unsupervised Learning 차이는?

### AI-03

Training과 Inference의 차이는?

### AI-04

Overfitting이 무엇인가요?

### AI-05

Neural Network란 무엇인가요?

### AI-06

Transformer는 왜 중요한가요?

### AI-07

Attention이 무엇인가요?

### AI-08

LLM이 무엇인가요?

### AI-09

Token이 무엇인가요?

### AI-10

Embedding이 무엇인가요?

---

# 12. RAG 문제

이건 1209에서 특히 중요합니다.

### RAG-01

LLM만 사용하는 것과 RAG를 사용하는 것의 차이는?

### RAG-02

Embedding이 필요한 이유는?

### RAG-03

Vector DB란?

### RAG-04

Cosine Similarity는 무엇을 측정하나요?

### RAG-05

Chunking을 하는 이유는?

### RAG-06

RAG 전체 흐름을 순서대로 쓰세요.

```
사용자 질문
→ ?
→ ?
→ ?
→ LLM
→ 답변
```

### RAG-07

회사 내부 규정 문서를 ChatGPT가 답하게 만들려고 합니다.

왜 Fine-tuning보다 RAG를 먼저 고려할 수 있을까요?

### RAG-08

RAG를 사용했는데 잘못된 답변이 나왔습니다.

가능한 원인을 3개 생각해보세요.

---

# 13. Agent 기초

여기까지는 **개강 전에 개념만** 알면 됩니다.

### Agent-01

일반 LLM과 AI Agent의 가장 큰 차이는?

### Agent-02

Tool Calling이 무엇인가요?

### Agent-03

다음 구조에서 Supervisor의 역할은?

```
             Supervisor
             /    |    \
        Search   SQL   Report
        Agent   Agent   Agent
```

### Agent-04

MCP가 왜 필요한지 아는 범위에서 설명하세요.

**현재는 코드까지 공부하지 마세요.**

---

# 14. 개강 전 우선순위

당신은 이 순서로 하는 게 효율적입니다.

```
★★★★★ Python
★★★★★ 면접
★★★★☆ Linux
★★★★☆ HTTP / REST
★★★★☆ Git 복습
★★★★☆ AI / LLM 기본
★★★☆☆ Docker
★★★☆☆ FastAPI
★★★☆☆ RAG
★★☆☆☆ SQL
★☆☆☆☆ LangGraph
★☆☆☆☆ MCP
★☆☆☆☆ Kubernetes
```

**LangGraph/MCP/Kubernetes를 지금 선행하지 않는 게 중요합니다.**

기초가 잡힌 후 수업에서 배우면 훨씬 빨리 이해됩니다.

---

# 15. 7일 압축 계획

### DAY 1 — Python

- 자료형
- list/dict/set/tuple
- 조건문/반복문
- 함수
- PY-01~05

### DAY 2 — Python

- Class/OOP
- 예외처리
- 파일
- List comprehension
- PY-06~10

### DAY 3 — Linux + Git

- Bandit 0~5
- Linux 문제
- Learn Git Branching
- Git 문제

### DAY 4 — HTTP + FastAPI

- HTTP Method
- Status Code
- JSON
- REST
- FastAPI-01~04

### DAY 5 — Docker

- Image/Container
- Dockerfile
- build/run
- Docker Compose
- FastAPI Dockerize

### DAY 6 — AI + LLM + RAG

AI-01~10

RAG-01~08

그리고 아래 구조를 **보지 않고 직접 그릴 수 있도록** 합니다.

```
Question
   ↓
Embedding
   ↓
Vector DB
   ↓
Retrieval
   ↓
Context
   ↓
LLM
   ↓
Answer
```

### DAY 7 — 모의면접 + 종합시험

면접 10문항을 **각각 40초~1분**으로 말해보기.

그리고:

```
Python 10문제
Linux 10문제
Git 7문제
HTTP 7문제
Docker 7문제
AI 10문제
RAG 8문제
```

를 답지 없이 풀어봅니다.

---

## 가장 중요한 목표

레벨테스트에서 **모든 걸 알고 있는 사람처럼 보일 필요는 없습니다.**

당신은 이미 개발 경험이 있기 때문에 면접관에게 보여줘야 할 그림은 이것입니다.

```
C++ / C#
Unity / Unreal
알고리즘 / OOP
팀 프로젝트 경험
        ↓
Python 빠르게 적응
        ↓
LLM / RAG / Agent 학습
        ↓
AI Software Engineer
```

특히 **Python + Linux + HTTP + AI/LLM/RAG 개념**까지 준비해두면 1209 레벨테스트와 초반 수업 모두 상당히 편해질 가능성이 높습니다.