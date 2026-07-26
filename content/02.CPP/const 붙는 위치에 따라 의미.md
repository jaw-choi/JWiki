
1. const 붙는 위치 핵심만 재정리
    

레퍼런스 기준

- const T& x : 대상 객체(T)의 상태를 못 바꿈
    
- T& const x : 레퍼런스는 재바인딩이 원천적으로 불가라서 의미 없음(붙여도 실익 0)
    

포인터 기준

- const T* p : p가 가리키는 대상(T) 수정 불가, p는 다른 주소로 바꿀 수 있음
    
- T* const p : p 자체(주소값) 변경 불가, 대상(T)은 수정 가능
    
- const T* const p : 둘 다 불가
    

멤버 함수 뒤 const

- T::Func() const : 이 함수 안에서 this가 가리키는 객체 상태를 못 바꿈(논리적 const)