## 문제 정의

shared_ptr로 소유된 객체들(vector 등)을 순회하면서 dynamic_cast로 특정 파생 타입을 찾는 패턴에서 성능 부담이 커지는 경우가 있음  
핵심 병목은 대개 아래 2가지로 수렴함

- 순회 중 shared_ptr 복사로 인한 ref_count 증가/감소(atomic inc/dec)가 반복 발생
    
- 캐스팅 결과를 shared_ptr로 추가 생성하면서 성공 케이스에서 ref_count 증가가 추가 발생
    

---

## atomic 부담이 발생하는 지점

### 1) range-for에서 shared_ptr을 값으로 받는 경우

- 매 반복마다 shared_ptr 복사 발생
    
- 복사/소멸 시 ref_count inc/dec가 매번 발생(보통 atomic)
    

나쁜 예

- for (auto sp : vec) { ... }
    

좋은 예

- for (const auto& sp : vec) { ... }
    

---

### 2) 캐스팅 결과를 shared_ptr로 매번 만들거나, 불필요하게 여러 번 만드는 경우

- 성공했을 때 shared_ptr 생성으로 ref_count 증가
    
- 루프 내부에서 결과를 계속 갱신/복사하면 증가/감소가 반복될 수 있음
    

---

## 해소 전략 (추천 우선순위)

## 1순위: shared_ptr 복사 제거 (range-for 참조로 받기)

- 순회 중 ref_count 변화가 0으로 수렴
    
- 가장 간단하면서 체감 효과가 큰 최우선 조치
    

체크 포인트

- for (const auto& sp : vec) 형태로 고정
    

---

## 2순위: 찾는 동안은 raw pointer로만 검사하고, 찾은 순간에만 shared_ptr 1회 증가

목표

- 루프 중에는 ref_count 변동 0
    
- 성공 시점에만 ref_count +1 딱 한 번
    

핵심 아이디어

- dynamic_cast는 sp.get()로 raw pointer에 대해 수행(증가 없음)
    
- 발견 순간에만 owner/result를 세팅해 shared_ptr을 1회만 증가
    

패턴 A: 소유 유지(shared_ptr) + 접근(raw*)

- 발견 순간: owner = sp 로 ref_count 1회 증가
    
- raw 포인터는 owner가 살아있는 동안만 사용
    

예시

`std::shared_ptr<Base> owner;   // 발견한 객체의 생존 보장 Derived* found = nullptr;      // 파생 타입 접근(비소유)  for (const auto& sp : vec) {     if (auto* p = dynamic_cast<Derived*>(sp.get())) {         owner = sp;   // ref_count +1 (딱 한 번)         found = p;    // 증가 없음         break;     } }  if (found) {     found->Special(); // owner가 살아있는 동안만 안전 }`

---

## 3순위: 파생 shared_ptr가 꼭 필요하면 성공 순간에만 aliasing 생성

상황

- 결과를 함수 밖으로 들고 나가야 함
    
- Derived shared_ptr이 필요함
    

핵심

- raw로 먼저 성공 여부 판단
    
- 성공 시점에만 aliasing constructor로 shared_ptr<Derived> 생성
    

예시

`std::shared_ptr<Derived> result;  for (const auto& sp : vec) {     if (auto* p = dynamic_cast<Derived*>(sp.get())) {         result = std::shared_ptr<Derived>(sp, p); // 성공 시점 1회 증가         break;     } }`

특징

- 루프 중 ref_count 변화 거의 0
    
- 성공 케이스에서만 1회 증가