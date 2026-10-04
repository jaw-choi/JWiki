# 메이플스토리 월드 AI Toolkit · 단풍 · 넥토리얼 면접 대비 정리

## 0. 문서 목적

이 문서는 다음 두 가지를 한 번에 정리하기 위한 자료다.

1. 넥슨의 **메이플스토리 월드(MapleStory Worlds, MSW) AI Toolkit / 단풍 / 바이브 코딩** 개념 이해
2. 이를 바탕으로 **넥토리얼을 통해 넥슨코리아 게임 개발 직무 면접을 본다고 가정한 예상 질문 대비**

특히 단순히 "AI를 써서 게임을 만들었다"가 아니라,

> **게임 시스템은 내가 설계하고, AI는 구현 속도를 높이는 도구로 활용했다**

는 방향으로 설명하는 것이 핵심이다.

---

# 1. MSW AI Toolkit이란?

넥슨은 메이플스토리 월드의 제작 진입장벽을 낮추기 위해 **MSW AI Toolkit**을 제공하고 있다.

메이플스토리 월드는 일반적인 Lua가 아니라 MSW 환경에 맞는 스크립트와 전용 API, Entity, Component 구조를 사용한다.

따라서 일반적인 LLM에게 코드를 요청할 경우 다음과 같은 문제가 발생할 수 있다.

- 일반 Lua 기준으로 코드를 생성
- 존재하지 않는 MSW API 생성
- MSW 프로젝트 구조와 맞지 않는 코드 생성
- Client / Server 실행 영역을 잘못 판단
- Component 간 책임을 잘못 나눔

이 문제를 줄이기 위해 넥슨은 MSW 개발에 특화된 AI 환경을 구축하고 있다.

---

# 2. ‘단풍’이란?

**단풍**은 메이플스토리 월드 개발 환경에 특화된 LLM이다.

일반적인 프로그래밍 지식뿐만 아니라 다음과 같은 MSW 개발 지식을 활용하는 것을 목표로 한다.

- MSW 스크립트 문법
- MSW API
- Entity 구조
- Component 구조
- Property
- Event
- Client / Server 구조
- 월드 제작 방식

즉 일반 LLM이

```text
Lua라면 보통 이런 식으로 구현하면 됩니다.
```

라고 답한다면,

단풍과 MSW AI 환경은

```text
MSW에서는 이 기능을 구현할 때
어떤 Component와 API를 사용하는 것이 적절한지
```

까지 이해하도록 특화되어 있다는 점이 중요하다.

---

# 3. 바이브 코딩이란?

바이브 코딩은 사용자가 자연어로 기능을 설명하고 AI가 코드 작성을 지원하는 개발 방식이다.

예를 들어 사용자가 다음과 같이 요청할 수 있다.

```text
몬스터를 죽이면
마지막으로 공격한 플레이어에게 경험치 10을 지급해줘.

경험치가 일정 수준 이상이면 레벨업시키고
레벨업할 때 공격력을 증가시켜줘.
```

AI는 이를 다음 구조로 해석할 수 있다.

```text
Monster Death Event
↓
공격한 Player 확인
↓
EXP 증가
↓
레벨업 조건 검사
↓
Level 증가
↓
Stat 증가
↓
UI 갱신
```

즉 자연어 요구사항을 실제 게임 시스템으로 변환하는 과정에서 AI가 개발자를 보조한다.

---

# 4. 중요한 점: 바이브 코딩 ≠ AI가 게임을 전부 만드는 것

게임 개발 면접에서는 이 부분이 매우 중요하다.

좋지 않은 설명:

> AI에게 게임을 만들어달라고 해서 만들었습니다.

좋은 설명:

> 게임의 구조와 시스템 책임은 제가 설계했고,
> 반복적인 구현과 API 탐색, 보일러플레이트 코드 작성에 AI를 활용했습니다.
> AI가 생성한 코드는 직접 검증하고 테스트했습니다.

AI는 다음 부분을 도울 수 있다.

```text
API 탐색
코드 초안 작성
반복 코드 생성
리팩터링 제안
에러 원인 추정
문서 검색
테스트 코드 작성
```

하지만 개발자가 결정해야 할 부분은 여전히 존재한다.

```text
게임 규칙
시스템 구조
상태 관리
Component 책임
데이터 구조
네트워크 구조
성능
예외 처리
게임 재미
```

---

# 5. MSW AI 개발 구조

전체적인 개발 흐름은 다음과 같이 이해하면 된다.

```text
개발자
↓
자연어 요구사항
↓
Cursor / Claude Code / Codex 등 AI Agent
↓
MSW AI Toolkit / MCP
↓
MSW API / 문서 / 프로젝트 Context
↓
mLua 코드 생성 및 수정
↓
MapleStory Worlds에서 실행
↓
테스트
↓
수정
```

핵심은 AI가 단순한 채팅 도구가 아니라

> **실제 개발 프로젝트의 Context를 이해하고 코드 작업을 보조하는 Agent**

로 확장되고 있다는 것이다.

---

# 6. MCP가 중요한 이유

MCP(Model Context Protocol)는 AI Agent가 외부 도구나 정보를 활용할 수 있도록 연결하는 구조라고 이해하면 된다.

MSW 개발에서는 AI가 다음 Context에 접근할 수 있어야 정확도가 높아진다.

```text
MSW 개발 문서
MSW API
프로젝트 파일
Entity 구조
Component 구조
기존 코드
```

즉 일반 ChatGPT에 단순히

```text
MSW 몬스터 AI 만들어줘
```

라고 요청하는 것보다,

프로젝트 Context와 MSW 정보를 AI Agent가 활용하게 만드는 것이 훨씬 효과적이다.

---

# 7. 직접 해볼 수 있는 방법

## STEP 1. MapleStory Worlds 설치

먼저 MapleStory Worlds를 설치한다.

처음에는 아주 작은 프로젝트로 시작하는 것이 좋다.

```text
Map
+
Player
+
Monster
+
Attack
+
EXP
```

정도면 충분하다.

---

# 8. LocalWorkspace 사용

AI Agent가 프로젝트 코드를 분석하려면 프로젝트 파일을 외부 개발 환경에서 접근할 수 있어야 한다.

예:

```text
MSW_Project/

├─ scripts/
├─ components/
├─ entities/
├─ ui/
└─ data/
```

이 구조를 Cursor나 VS Code 같은 환경에서 열고 AI Agent가 분석하도록 할 수 있다.

---

# 9. 첫 번째 AI 요청 예시

```text
현재 프로젝트 구조를 먼저 분석해줘.

몬스터가 죽을 때
마지막으로 공격한 플레이어에게 EXP 10을 지급하는
시스템을 구현하고 싶다.

조건

1. MSW 환경에 맞는 문법을 사용한다.
2. 실제 존재하는 MSW API를 사용한다.
3. 기존 코드 구조를 최대한 유지한다.
4. 변경해야 할 Component를 먼저 설명한다.
5. 구현 후 발생할 수 있는 예외 상황도 설명한다.
```

이런 식으로 요청하면 단순 코드 생성보다 품질이 좋아진다.

---

# 10. 추천 실습 프로젝트: 메이플 로그라이크

첫 프로젝트로는 **Vampire Survivors 형태의 메이플 로그라이크**가 적합하다.

게임 흐름:

```text
게임 시작
↓
몬스터 등장
↓
몬스터 처치
↓
EXP 획득
↓
레벨업
↓
3가지 능력 중 하나 선택
↓
캐릭터 강화
↓
다음 웨이브
↓
10분 생존
↓
보스 등장
```

이 프로젝트의 장점은 다양한 게임 클라이언트 시스템을 한 번에 연습할 수 있다는 것이다.

---

# 11. 구현할 시스템

## 11.1 Player

```text
Movement
Attack
HP
EXP
Level
Stat
Skill
```

## 11.2 Monster

```text
Spawn
Move
Targeting
Attack
HP
Death
Reward
```

## 11.3 Game

```text
Wave
Timer
Difficulty
Boss
GameOver
Result
```

## 11.4 UI

```text
HP Bar
EXP Bar
Level
Skill Selection
Timer
Boss HP
```

---

# 12. 몬스터 스폰 시스템 프롬프트

```text
플레이어 주변 일정 거리 밖에서
3초마다 몬스터를 생성해줘.

조건

최대 몬스터 수는 30마리다.

몬스터가 30마리 이상 존재하면
추가 Spawn을 하지 않는다.

플레이어 화면 바로 앞에서 생성되지 않도록
최소 Spawn 거리를 둔다.
```

---

# 13. 경험치 시스템

```text
몬스터를 처치하면 경험치를 지급한다.

필요 경험치는 다음 식을 사용한다.

RequiredEXP = 100 + Level * 20

현재 EXP가 RequiredEXP를 초과하면
Level을 증가시킨다.

남은 EXP는 유지한다.
```

중요한 예외:

```text
한 번에 많은 EXP를 얻어서
2레벨 이상 상승할 수 있는 경우
```

따라서 단순 if가 아니라 while 방식도 고려할 수 있다.

---

# 14. Skill 선택 시스템

레벨업 시 랜덤 능력 3개를 제시한다.

예:

```text
Attack +10%
Attack Speed +10%
Move Speed +10%
Critical Rate +5%
Projectile Count +1
```

게임 흐름:

```text
Level Up
↓
Skill Pool
↓
Random 3개 선택
↓
UI 표시
↓
Player 선택
↓
Stat 적용
```

---

# 15. 보스 AI

좋지 않은 요청:

```text
보스 만들어줘.
```

좋은 요청:

```text
BossComponent를 만들어줘.

HP: 5000

State

Idle
Chase
Attack
Dead

패턴 1

플레이어와 거리가 5m 이상이면
플레이어를 추적한다.

패턴 2

3초마다 플레이어 방향으로 투사체를 발사한다.

패턴 3

HP가 50% 이하이면
투사체를 3방향으로 발사한다.

먼저 State 구조와 Component 책임을 설계한 뒤
코드를 작성해줘.
```

---

# 16. 바이브 코딩을 잘하는 방법

좋은 AI 프롬프트는 다음 정보를 포함한다.

```text
목표
조건
현재 구조
데이터
예외 상황
성능 제약
변경 범위
```

예:

```text
Player Dash 시스템을 만들어줘.

Dash Distance: 5m
Cooldown: 3 sec
Dash Duration: 0.3 sec

Dash 중에는 피해를 받지 않는다.

Cooldown 중에는 다시 사용할 수 없다.

기존 PlayerMovementComponent를 최대한 유지한다.

UI에는 남은 Cooldown을 표시한다.
```

---

# 17. 게임 개발자가 반드시 확인해야 할 부분

AI가 코드를 작성했다고 바로 사용하는 것은 위험하다.

반드시 다음을 확인해야 한다.

## API 유효성

실제로 존재하는 API인가?

## 실행 위치

Client에서 실행해야 하는가?

Server에서 실행해야 하는가?

## 상태 관리

State가 여러 Component에 중복 저장되어 있지 않은가?

## Event

Event가 중복 호출될 가능성이 없는가?

## 성능

Update에서 매 프레임 불필요한 탐색을 하고 있지 않은가?

## Entity 생성

몬스터 Spawn / Destroy가 지나치게 자주 발생하지 않는가?

## 네트워크

Client가 수정하면 안 되는 중요한 데이터를 Client가 변경하고 있지 않은가?

---

# 18. 포트폴리오에 넣는 방법

## 프로젝트명

**MapleStory Worlds AI-Assisted Roguelike**

## 문제

MSW는 독자적인 개발 환경과 API를 가지고 있기 때문에 초기 학습 비용이 존재한다.

## 접근

```text
MSW AI Toolkit
+
MCP
+
AI Coding Agent
```

를 사용하여 API 탐색과 코드 구현 속도를 높였다.

## 직접 설계한 부분

```text
Game Loop
Entity 구조
Component 책임
Monster State Machine
Wave System
Skill System
EXP System
Boss Pattern
```

## AI를 활용한 부분

```text
API 탐색
코드 초안
반복 코드
리팩터링
디버깅 보조
문서 검색
```

## 개발 과정

```text
요구사항 정의
↓
시스템 설계
↓
AI 코드 생성
↓
코드 리뷰
↓
테스트
↓
버그 수정
↓
리팩터링
↓
최적화
```

---

# 19. 넥토리얼 면접에서 이 프로젝트를 설명하는 방법

면접에서는 AI를 썼다는 사실 자체보다

> **AI를 어떻게 통제하고 검증했는가**

가 중요하다.

추천 설명:

```text
MSW 개발 과정에서 AI Toolkit을 활용했습니다.

하지만 게임 구조를 AI에게 전부 맡기지는 않았습니다.

먼저 제가 Entity와 Component 책임,
Monster State,
Wave System,
EXP 및 Skill 구조를 설계했습니다.

그 이후 반복적인 구현이나
MSW API 탐색에 AI를 활용했습니다.

AI가 작성한 코드는 실제 API 여부와
Client / Server 실행 위치,
Event 중복 호출,
성능 문제 등을 직접 검증했습니다.
```

---

# 20. 넥토리얼 / 넥슨코리아 면접 예상 질문

아래 질문들은 실제 기출이라고 단정하는 것이 아니라,
**게임 클라이언트 개발 직무와 AI 활용 프로젝트를 기준으로 예상할 수 있는 질문**이다.

---

# 21. 프로젝트 기본 질문

## Q1. 이 프로젝트를 왜 만들었나요?

답변 방향:

```text
MSW AI Toolkit이 실제 게임 개발 생산성을
얼마나 높일 수 있는지 직접 확인하고 싶었다.

단순 예제가 아니라
전투 / 몬스터 / 경험치 / Skill / Wave 등
게임 클라이언트의 기본 시스템이 포함된
로그라이크를 구현했다.
```

---

## Q2. 가장 어려웠던 부분은 무엇인가요?

추천 소재:

```text
Component 책임 분리
Monster 수 증가에 따른 성능
Event 처리
AI가 생성한 잘못된 API
Client / Server 데이터 동기화
```

답변 구조:

```text
문제
↓
원인 분석
↓
해결
↓
결과
```

---

## Q3. AI 없이 만들 수 있었나요?

좋은 답변:

> 가능하지만 개발 속도에 차이가 있었습니다.  
> 기본 구조와 로직은 제가 설계할 수 있었고, AI는 API 탐색과 반복적인 코드 구현 시간을 줄이는 데 사용했습니다.

피해야 할 답변:

> AI 없으면 못 만들었을 것 같습니다.

---

# 22. AI 관련 예상 질문

## Q4. AI가 작성한 코드를 어떻게 신뢰했나요?

핵심:

> 신뢰하지 않고 검증했다.

검증 항목:

```text
API 존재 여부
Parameter
Return Type
Client / Server
Null 가능성
Event Lifecycle
성능
```

---

## Q5. AI가 잘못된 코드를 생성한 경험이 있나요?

좋은 답변 구조:

```text
AI가 존재하지 않는 API를 제안했다.
↓
공식 문서와 프로젝트 Context를 확인했다.
↓
실제 API로 교체했다.
↓
이후 프롬프트에
"실제 MSW API만 사용할 것"이라는 조건을 추가했다.
```

---

## Q6. AI가 개발자의 역할을 대체할 수 있다고 생각하나요?

추천 방향:

```text
구현 속도는 크게 향상시킬 수 있다.

하지만

시스템 설계
Trade-off 판단
게임 재미
성능
디버깅
Architecture

같은 영역은 여전히 개발자의 판단이 중요하다.
```

---

# 23. 바이브 코딩 관련 꼬리 질문

## Q7. 바이브 코딩의 가장 큰 위험은 무엇인가요?

예상 답:

```text
코드를 이해하지 않고 누적시키는 것
```

결과:

```text
기술 부채 증가
Architecture 붕괴
중복 State
불필요한 Dependency
Debug 어려움
```

---

## Q8. AI가 생성한 코드가 동작하면 그대로 사용해도 되나요?

아니다.

확인해야 할 것:

```text
Correctness
Readability
Maintainability
Performance
Security
Networking
```

---

# 24. 게임 클라이언트 기술 질문

## Q9. Update에서 모든 몬스터가 Player를 찾으면 어떤 문제가 생기나요?

몬스터 수를 N이라고 하면
매 프레임 탐색 비용이 증가한다.

개선 방법:

```text
Player Reference Cache
Event 기반 처리
Spatial Partition
Update 주기 분산
Distance Check 최소화
```

---

## Q10. Object Pooling을 왜 사용하나요?

총알이나 몬스터처럼 자주 생성/삭제되는 객체는

```text
Create
Destroy
Create
Destroy
```

를 반복하면 비용이 증가한다.

Object Pool:

```text
미리 생성
↓
사용
↓
비활성
↓
재사용
```

장점:

```text
Allocation 감소
GC 부담 감소
Frame Drop 감소
```

---

# 25. 자료구조 예상 질문

## Q11. 몬스터를 관리한다면 vector와 list 중 무엇을 쓰겠나요?

정답 하나가 있는 문제는 아니다.

대부분 게임 상황에서는 cache locality 때문에

```text
vector
```

가 유리할 수 있다.

하지만 삭제 패턴과 데이터 구조에 따라 달라진다.

면접에서는

> 데이터 접근 패턴을 먼저 보겠습니다.

라고 시작하는 것이 좋다.

---

# 26. C++ 예상 질문

## Q12. virtual 함수는 어떻게 동작하나요?

핵심:

```text
vtable
vptr
dynamic dispatch
```

파생 클래스에서 Override된 함수가
Runtime에 선택된다.

---

## Q13. unique_ptr과 shared_ptr 차이는?

### unique_ptr

```text
소유권 1개
가볍다
move 가능
```

### shared_ptr

```text
Reference Count
여러 객체가 공동 소유
```

게임 개발에서는 무분별한 shared_ptr 사용이 성능과 Lifetime 추적을 어렵게 만들 수 있다.

---

# 27. 메모리 관련 질문

## Q14. Stack과 Heap 차이는?

Stack:

```text
빠른 Allocation
함수 Scope 기반
크기 제한
```

Heap:

```text
동적 Allocation
Lifetime 직접 관리
비용 상대적으로 큼
```

---

# 28. 게임 루프 예상 질문

## Q15. Fixed Update와 일반 Update를 왜 구분하나요?

Frame Rate와 독립적으로 일정 시간 간격 계산이 필요한 시스템이 있기 때문이다.

대표:

```text
Physics
```

렌더링:

```text
Frame 기반
```

물리:

```text
Fixed Time Step
```

---

# 29. Delta Time 질문

## Q16. 이동할 때 Delta Time을 곱하는 이유는?

```text
position += speed * deltaTime
```

Frame Rate가 달라도 초당 이동 거리를 일정하게 만들기 위해서다.

---

# 30. 충돌 질문

## Q17. 충돌 검사를 모든 객체끼리 하면 어떤 문제가 있나요?

객체 수가 N이면 단순 방식은

```text
O(N²)
```

수준까지 증가할 수 있다.

개선:

```text
Grid
QuadTree
BVH
Spatial Hash
```

---

# 31. FSM 관련 질문

## Q18. 보스 AI에 FSM을 사용한 이유는?

상태가 명확하기 때문이다.

```text
Idle
Chase
Attack
Dead
```

장점:

```text
상태 전환 명확
Debug 용이
Logic 분리
```

---

# 32. FSM의 단점은?

상태와 조건이 많아지면

```text
State Explosion
```

이 발생할 수 있다.

대안:

```text
Behavior Tree
Hierarchical FSM
Utility AI
```

---

# 33. 네트워크 예상 질문

## Q19. Player HP를 Client가 직접 결정하면 어떤 문제가 발생하나요?

Client 조작 가능성이 생긴다.

따라서 중요한 게임 상태는 보통

```text
Server Authoritative
```

구조를 고려해야 한다.

---

# 34. Client와 Server 역할

예:

Client:

```text
Input
UI
Animation
Effect
Prediction
```

Server:

```text
Game Rule
Damage
HP
Reward
Inventory
Validation
```

게임 특성에 따라 달라질 수 있다.

---

# 35. 성능 최적화 질문

## Q20. 몬스터가 30마리에서 300마리로 증가하자 FPS가 떨어졌습니다. 어떻게 분석하겠나요?

좋은 접근:

```text
Profiler 확인
↓
CPU / GPU 구분
↓
Update 비용
↓
Physics
↓
Draw Call
↓
Allocation / GC
↓
Network
```

추측부터 하지 않고

> Profile → Bottleneck 확인 → 최적화

순서를 강조하는 것이 좋다.

---

# 36. 넥슨 면접에서 나올 수 있는 게임 질문

## Q21. 최근 재미있게 플레이한 게임은?

단순 감상보다 시스템 분석이 중요하다.

예:

```text
재미 요소
↓
게임 Loop
↓
보상 구조
↓
난이도
↓
Retention
```

---

## Q22. 메이플스토리의 핵심 재미는 무엇이라고 생각하나요?

가능한 관점:

```text
성장
수집
전투
커뮤니티
경제
캐릭터 Identity
장기 Progression
```

한 가지를 선택하고 논리적으로 설명하는 것이 좋다.

---

# 37. MSW 관련 예상 질문

## Q23. Roblox와 MapleStory Worlds의 차이는 무엇이라고 생각하나요?

답변 방향 예:

```text
Roblox
→ 독립적인 UGC Platform

MSW
→ MapleStory라는 강력한 IP Asset과
Creator 생태계를 결합
```

MSW는 기존 메이플스토리 이용자가 익숙한

```text
Character
Monster
Map
Asset
Gameplay
```

을 활용할 수 있다는 장점이 있다.

---

# 38. 왜 넥슨인가?

## Q24. 다른 게임 회사가 아니라 넥슨에 지원한 이유는?

피해야 할 답:

```text
게임을 좋아해서
메이플을 좋아해서
큰 회사라서
```

추천 구조:

```text
넥슨이 시도하는 기술
+
내 경험
+
내가 하고 싶은 개발
```

예:

> 넥슨은 라이브 게임뿐 아니라 MSW처럼 이용자가 직접 콘텐츠를 만드는 플랫폼과 AI 기반 개발 도구까지 확장하고 있습니다.  
> 저는 게임 클라이언트 개발과 AI 개발 도구 활용 경험을 함께 발전시키고 싶어 지원했습니다.

---

# 39. 넥토리얼 지원동기 예상 질문

## Q25. 왜 신입 공채가 아니라 넥토리얼인가요?

추천 방향:

```text
실제 개발 조직에서
코드 리뷰
협업
라이브 프로젝트
개발 프로세스

를 경험하고 싶었다.
```

---

# 40. 협업 질문

## Q26. 팀원과 기술적인 의견이 충돌하면 어떻게 하나요?

답변 구조:

```text
문제 정의
↓
각 방식의 장단점 정리
↓
측정 가능한 기준 설정
↓
Prototype / Benchmark
↓
팀 기준으로 결정
```

감정이 아니라 근거로 해결한다는 점이 중요하다.

---

# 41. 코드 리뷰 질문

## Q27. 코드 리뷰에서 가장 중요하게 보는 것은?

예:

```text
Correctness
Readability
Responsibility
Dependency
Edge Case
Performance
```

모든 코드를 성능만 보고 리뷰하지 않는다.

---

# 42. 실패 경험

## Q28. 개발하면서 실패했던 경험을 이야기해주세요.

좋은 실패 경험:

```text
기술 선택 실패
Architecture 과설계
성능 문제
일정 예측 실패
협업 문제
```

답변 구조:

```text
상황
↓
내 판단
↓
문제 발생
↓
수정
↓
배운 점
```

---

# 43. 가장 중요한 꼬리 질문

면접관은 프로젝트 설명 후 보통

```text
왜?
```

를 반복한다.

예:

```text
왜 Component로 분리했나요?

왜 Singleton을 사용했나요?

왜 Event를 사용했나요?

왜 vector를 사용했나요?

왜 AI에게 이 부분을 맡겼나요?

왜 Server에서 처리했나요?
```

따라서 모든 기술 선택에 대해

```text
장점
단점
대안
선택 이유
```

를 준비해야 한다.

---

# 44. MSW 프로젝트 면접 준비 체크리스트

다음 질문은 반드시 답할 수 있어야 한다.

- 게임의 전체 Architecture를 설명할 수 있는가?
- 핵심 Component를 설명할 수 있는가?
- 가장 어려웠던 버그는 무엇인가?
- AI가 잘못 생성한 코드 사례가 있는가?
- 직접 작성한 코드와 AI 코드의 차이는 무엇인가?
- 성능 문제를 어떻게 확인했는가?
- Monster 수가 10배 증가하면 어떤 문제가 생기는가?
- Multiplayer라면 구조를 어떻게 바꿀 것인가?
- Save System을 어떻게 설계할 것인가?
- Server와 Client 역할을 어떻게 나눌 것인가?
- AI를 제거해도 프로젝트를 유지보수할 수 있는가?

---

# 45. 포트폴리오 발표 구조

면접 발표가 있다면 다음 구조를 추천한다.

## 1. 프로젝트 목표

```text
AI Toolkit을 활용한
MSW 로그라이크 제작
```

## 2. 게임 영상

약 30초

```text
Combat
Level Up
Skill
Wave
Boss
```

## 3. Architecture

```text
Player
Monster
Game
UI
```

## 4. 핵심 구현

```text
FSM
Wave
Skill
EXP
```

## 5. AI 활용

```text
어디에 사용했는가?
왜 사용했는가?
어떻게 검증했는가?
```

## 6. 문제 해결

가장 어려웠던 버그 1~2개

## 7. 성능 개선

Before / After

## 8. 배운 점

```text
AI 활용
Architecture
Debugging
Game Development
```

---

# 46. 면접에서 좋은 인상을 주는 한 문장

AI 활용 프로젝트를 설명할 때 핵심 메시지는 다음과 같다.

> **AI가 코드를 대신 작성하게 한 것이 아니라, 제가 설계한 게임 시스템을 더 빠르게 구현하고 검증하기 위한 개발 도구로 사용했습니다.**

---

# 47. 실제 면접 직전 준비 방법

## 1단계

프로젝트를 3분 안에 설명한다.

## 2단계

Architecture를 그림 없이 설명해본다.

## 3단계

각 기술 선택에 대해

```text
왜?
```

를 최소 3번 스스로 질문한다.

## 4단계

AI가 생성한 코드 중

```text
틀렸던 코드
수정한 코드
```

를 하나 준비한다.

## 5단계

성능 문제 하나를 준비한다.

## 6단계

가장 어려웠던 버그 하나를 준비한다.

---

# 48. 최종 정리

MSW AI Toolkit의 핵심은 단순 코드 자동 생성이 아니다.

```text
게임 개발 지식
+
MSW Context
+
AI Agent
```

를 결합해 개발 생산성을 높이는 것이다.

게임 개발자가 AI 시대에 가져야 할 경쟁력은

```text
코드를 얼마나 빨리 타이핑하는가
```

보다

```text
문제를 정의하고
시스템을 설계하고
AI 결과를 검증하고
문제를 해결하는 능력
```

에 가까워지고 있다.

넥슨 게임 개발 면접에서도 AI 사용 자체보다

> **게임 개발 기본기 + 시스템 설계 + 문제 해결 + AI 활용 능력**

을 함께 보여주는 것이 중요하다.
