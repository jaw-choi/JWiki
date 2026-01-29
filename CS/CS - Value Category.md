### L-Value

- 메모리 위치를 가지며, 수정이 가능하다.
- 일반적으로 변수나 객체를 나타낸다.
- 아래 코드에서 x는 L-Value다.
- x는 메모리 주소를 가지며, 값을 읽고 수정할 수 있다.

```cpp
int main()
{
	int x = 10;
	int y = x;
}
```
### L-Value Reference

- L-Value를 참조하는 데 사용한다. ==C++ 문법에서 레퍼런스라고 지칭하는 것이 L-Value Reference==다.
- ref 변수는 x 변수를 참조한다. x 변수는 메모리 주소를 가지며 읽고, 쓸 수 있는 L-Value이기 때문에 L-Value Reference로 선언이 가능하다.
- ref2 변수는 10을 참조한다. 하지만, 10은 메모리 주소가 없는 임시 값으로서 R-Value에 해당한다. L-Value Reference는 R-Value를 참조할 수 없기 때문에 오류가 발생한다.

```cpp
int main()
{
	int x = 10;
	int& ref = x;
	
	int& ref2 = 10;    // 오류 발생.
}
```
### R-Value

- 임시 값으로서 메모리에 저장되지 않고 즉시 사용된다.
- 아래 코드에서 x + 5는 메모리에 저장되지 않고, 임시 값으로 사용된 후 사라진다.

```cpp
int main()
{
	//10 = 3;
	int x = 10;
	int y = x + 5;
}
```
### R-Value Reference

- R-Value Reference는 C++ 11에서 도입되었다.
- R-Value Reference는 R-Value를 참조할 때 사용한다.
- L-Value Reference와 구분하기 위해 &대신 &&를 사용해 선언한다.
- 아래 코드에서 ref는 R-Value인 10을 참조하는 R-Value Reference다.
- R-Value Reference는 임시 값을 다른 어딘가에 저장하는 목적으로 많이 활용된다. 이때 값을 복사(Copy)하는 대신 이동(Move)하는 방법으로 속도를 향상시킬 수 있다.

```cpp
int main()
{
	int&& ref = 10;
}
```
ref가 임시공간을 가르킴


1. 값 카테고리(Value Category): lvalue / rvalue / 참조
    

- lvalue
    
    - “이름이 있고, 주소가 있고, 보통 수정 가능한” 값(변수 같은 것)
        
- rvalue
    
    - “임시 값” 성격이 강한 값(리터럴 10, x+5 같은 식의 결과)
        
- lvalue reference (T&)
    
    - lvalue를 참조하는 레퍼런스(전통적인 레퍼런스)
        
- rvalue reference (T&&)
    
    - rvalue(임시 값)를 참조하는 레퍼런스
        
    - 핵심 목적: 복사 대신 이동(move) 최적화를 가능하게 하는 문법적 장치
        
- 이동(move) 직관 정리
    
    - “메모리가 실제로 순간이동한다”라기보다,
        
    - “곧 사라질 임시 자원의 소유권을 새 주인이 가져가도록 설계”하는 쪽이 정확합니다.
        
- 혼동 포인트(강의에서 언급한 부분)
    
    - const가 붙으면 주소는 있어도 수정이 안 되므로, 단순한 ‘수정 가능 lvalue’ 정의만으로는 분류가 꼬입니다.
        
    - 그래서 현대 C++은 glvalue/prvalue/xvalue 같은 세분화가 있고, 그 위에서 참조 바인딩 규칙이 정리됩니다.
        
    - ==면접에서 자주 묻는 건 보통: “왜 T&&가 필요한가”, “move가 실제로 뭘 바꾸는가”, “복사/이동 생성자 차이”입니다.==