좋습니다. 지금부터는 설명식이 아니라 **실제 응시처럼** 진행하겠습니다. 제가 `시험 시스템 + AI Assistant + 평가자` 역할을 맡겠습니다.

넥슨이 공개한 설명처럼 **문제 파악 → 해결 순서 구조화 → AI 활용 → 검증 → 결과물**을 함께 보겠습니다. 특히 AI에게 단순히 “고쳐줘”라고 하는 것보다, 본인이 문제를 이해하고 방향을 잡은 뒤 AI와 계속 검증하는 과정을 중요하게 보겠습니다. 붙여넣은 텍스트(1) 붙여넣은 텍스트(1)

# C++ AI 활용 역량평가 — 모의테스트 1

**직무:** 게임 프로그래머  
**난이도:** 신입 ~ 인턴  
**권장 시간:** 60분  
**언어:** C++17  
**목표:** 버그 분석 + AI 활용 + 코드 수정 + 테스트

이번에는 제가 중간에 답을 알려드리지 않습니다.  
실제로 시험을 치듯 진행한 뒤 마지막에 **100점 기준 상세 평가표**로 채점하겠습니다.

---

## 상황

게임 캐릭터의 이동 속도를 관리하는 코드입니다.

기본 이동 속도는 `5.0`이며 다음 두 효과가 존재합니다.

- Sprint 상태: 이동속도 × `1.5`
- Slow 디버프: 이동속도 × `0.5`

두 효과는 **동시에 적용될 수 있습니다.**

그런데 QA에서 다음 버그가 발견됐습니다.

> Slow 상태에서 Sprint를 시작한 뒤 Sprint를 종료하면  
> 캐릭터의 이동속도가 정상 값으로 돌아오지 않는다.

---

# 제공 코드

```
#include <iostream>

enum class MoveState
{
    Idle,
    Sprint
};

class PlayerMovement
{
private:
    float baseSpeed = 5.0f;
    float currentSpeed = 5.0f;

    MoveState state = MoveState::Idle;
    bool slowed = false;

public:
    void EnterSprint()
    {
        state = MoveState::Sprint;
        currentSpeed *= 1.5f;
    }

    void ExitSprint()
    {
        state = MoveState::Idle;
        currentSpeed = baseSpeed;
    }

    void ApplySlow()
    {
        slowed = true;
        currentSpeed *= 0.5f;
    }

    void RemoveSlow()
    {
        slowed = false;
        currentSpeed = baseSpeed;
    }

    float GetSpeed() const
    {
        return currentSpeed;
    }
};

int main()
{
    PlayerMovement player;

    player.ApplySlow();

    std::cout << player.GetSpeed() << '\n';

    player.EnterSprint();

    std::cout << player.GetSpeed() << '\n';

    player.ExitSprint();

    std::cout << player.GetSpeed() << '\n';
}
```

현재 출력:

```
2.5
3.75
5
```

하지만 기대 출력은:

```
2.5
3.75
2.5
```

---

# 추가 요구사항

단순히 위 사례 하나만 맞춰서는 안 됩니다.

다음 조건을 모두 만족해야 합니다.

### 요구사항 A

아무 효과가 없으면:

```
speed = 5.0
```

### 요구사항 B

Sprint만 적용:

```
5.0 × 1.5 = 7.5
```

### 요구사항 C

Slow만 적용:

```
5.0 × 0.5 = 2.5
```

### 요구사항 D

Sprint + Slow:

```
5.0 × 1.5 × 0.5 = 3.75
```

### 요구사항 E

효과의 적용 순서에 따라 결과가 달라지면 안 됩니다.

즉,

```
Slow → Sprint
```

와

```
Sprint → Slow
```

는 모두 `3.75`가 되어야 합니다.

### 요구사항 F

다음처럼 함수가 실수로 여러 번 호출되더라도 효과가 중복 적용되면 안 됩니다.

```
player.EnterSprint();
player.EnterSprint();
```

결과는 `11.25`가 아니라:

```
7.5
```

여야 합니다.

마찬가지로:

```
player.ApplySlow();
player.ApplySlow();
```

도 `1.25`가 아니라:

```
2.5
```

여야 합니다.

---

# 제약조건

다음 public API는 그대로 유지하십시오.

```
EnterSprint()
ExitSprint()
ApplySlow()
RemoveSlow()
GetSpeed()
```

private 함수나 멤버 변수는 추가하거나 수정할 수 있습니다.

외부 라이브러리는 사용하지 않습니다.

---

# 시험 진행 방식

이번 모의평가는 총 5단계입니다.

**1단계 — 문제 파악**  
본인이 먼저 버그의 원인을 분석합니다.

**2단계 — AI Assistant 활용**  
저에게 필요한 질문을 합니다. 실제 AI 코딩 도우미처럼 답하겠습니다.

**3단계 — 해결 전략 결정**  
AI 답변을 그대로 사용하지 말고 어떤 방법을 선택할지 결정합니다.

**4단계 — 코드 수정**  
최종 C++ 코드를 제출합니다.

**5단계 — 검증 및 채점**  
제가 엣지 케이스를 테스트하고 평가합니다.

---

# 평가표

|평가 요소|배점|
|---|---|
|문제를 정확하게 정의했는가|15|
|원인 분석 및 가설 설정|15|
|문제를 단계적으로 구조화했는가|15|
|AI에게 적절한 질문을 했는가|15|
|AI 답변을 비판적으로 검증했는가|10|
|C++ 코드의 정확성|15|
|엣지 케이스 처리|10|
|설명 및 커뮤니케이션|5|
|**총점**|**100**|

---

# 🔴 STEP 1 — 지금부터 시험 시작

**아직 코드를 수정하지 마십시오.**

먼저 아래 세 가지에 답해주세요.

### Q1.

현재 코드에서 버그가 발생하는 **근본적인 원인**은 무엇이라고 생각하십니까?
removeslow 함수 호출의 부재

### Q2.

`ExitSprint()`만 다음처럼 바꾸는 해결책은 충분할까요?

```
void ExitSprint()
{
    state = MoveState::Idle;

    if (slowed)
        currentSpeed = baseSpeed * 0.5f;
    else
        currentSpeed = baseSpeed;
}
```

충분하다 / 충분하지 않다를 결정하고 **이유**를 설명해주세요.
충분하지 않다. slowed를 체크는 했지만 상태변화 코드가 없기 때문에 다시 버그가 발생할것이다.

### Q3.

이 문제를 해결하기 위해 AI Assistant에게 **첫 번째로 어떤 질문을 하시겠습니까?**

실제 시험이라고 생각하고 프롬프트를 직접 작성해주세요.

예를 들어 제가 원하는 건 이런 단순 질문이 아닙니다.

```
코드 고쳐줘.
```

본인이 문제를 어떻게 이해하고 있는지가 드러나는 프롬프트를 작성해보세요.
현재 내가 파악한 문제의 근본적인 원인은 removeslow 함수의 호출 부재이다. 이 함수에는 slowed 값, 즉 상태변화 코드가 있지만 다른 함수에서는 이 값을 확인하지 않고 진행하기 때문에 버그가 발생한다. 또한 slowed라고 따로 bool 값을 만드는것이 아니라 이미 가지고 있는 State에 slowed를 추가해서 좀더 명시적이게 바꾸려 한다. 이후에 각 state에 들어설 때나 벗어날 때 항상 state값을 확인하는 코드를 추가하여 코드를 수정하려한다. 

**Q1 / Q2 / Q3 순서대로 답해주시면, 그 순간부터 제가 시험장 안의 AI Assistant처럼 답하면서 2단계로 진행하겠습니다.**