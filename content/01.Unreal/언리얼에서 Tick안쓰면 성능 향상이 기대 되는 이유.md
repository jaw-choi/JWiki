# 🔥 1. 함수 호출 자체 비용

```
void AMyActor::Tick(float DeltaTime){    // 아무것도 안 해도 호출됨}
```

👉 “내용이 없어도” 비용이 발생합니다.

- 함수 호출 오버헤드
- 가상 함수(Virtual) 디스패치
- 수많은 Actor/Component 반복

📌 예시

- Actor 1,000개 × 60FPS  
    👉 **초당 60,000번 호출**

---

# 🧠 2. 캐시 효율 (진짜 중요한 포인트)

Tick이 많아지면:

- 객체들이 메모리 여기저기 흩어짐
- CPU 캐시 miss 증가

👉 결과:

- **CPU가 계속 메모리 다시 읽음**
- 체감 성능 크게 떨어짐

---

# ⚙️ 3. 내부적으로 Tick 관리 비용 존재

언리얼은 Tick을 이렇게 관리합니다:

- Tick Group 분류
- 실행 순서 정렬
- 활성/비활성 체크

👉 Tick 많을수록  
**엔진 내부 스케줄링 비용 증가**

---

# 🧨 4. “아무것도 안 하는 Tick”도 비용이다

많이 하는 실수:

```
if (!bIsActive) return;
```

👉 이렇게 해도 이미:

- Tick 호출됨
- 조건 체크 수행됨

즉,  
👉 **“이미 늦음”**

---

# ⚡ 그래서 안 쓰면 뭐가 좋아지나

## ✔ CPU 사용량 감소

- 불필요한 반복 제거

## ✔ 캐시 효율 증가

- 메모리 접근 최적화

## ✔ 프레임 안정성 상승

- 스파이크 감소

---

# 🎯 대체 방법 (실무 핵심)

## 1. 이벤트 기반으로 전환

❌ Tick 방식

```
Tick에서 계속 상태 체크
```

✅ 이벤트 방식

```
OnDamage()OnOverlap()OnStateChanged()
```

👉 “필요할 때만 실행”

---

## 2. Timer 사용

```
GetWorld()->GetTimerManager().SetTimer(Handle, this, &AMyActor::Update, 1.0f, true);
```

👉 매 프레임 ❌  
👉 일정 간격 ✔

---

## 3. Tick 조건부 활성화

```
PrimaryActorTick.bCanEverTick = false;
```

필요할 때만:

```
SetActorTickEnabled(true);
```

---

## 4. Component 단위로 분리

👉 꼭 필요한 애만 Tick

---

# 🧠 Unity랑 차이 핵심

- **Unity**
    - Update 자동 관리 + 최적화 많이 되어 있음
    - 안 쓰면 호출 자체 안 됨
- **Unreal**
    - Tick = 명시적 등록 시스템
    - 개발자가 직접 제어

👉 그래서:  
**“엔진 이해를 강제하는 구조”**

---

# ⚡ 한 줄 핵심

👉 **“Tick은 편하지만, 가장 비싼 루프다”**

---

# 💡 실전 기준 판단

## ✔ Tick 써도 되는 경우

- 매 프레임 필요한 계산 (카메라, 입력, 물리 보정)

## ❌ 피해야 하는 경우

- 상태 체크용 로직
- 간헐적 이벤트
- AI 조건 검사