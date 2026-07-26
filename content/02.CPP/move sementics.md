==Move는 얕은 복사!==
![[Pasted image 20260129185200.png]]
Move Semantics는 메모리상의 이동을 의미
- Move Semantics를 사용하기 위해 Move 생성자, Move 대입 연산자를 도입
- Move 생성자, Move 대입 연산자의 인자는 R-Value 참조(&&)
- 클래스를 정의할 때 Move 생성자, Move 대입 연산자를 정의하면 Move Semantics를 사용할 수 있다.
- Move 생성자, Move 대입 연산자는 암묵적으로는 생성되지 않는다.
- 복사 생성자가 Move 생성자보다 우선순위가 높다.
- 대입 연산자가 Move 대입 연산자보다 우선순위가 높다.
참조의 행위는 복사이다

std::move(lvalue) => lvalue를 rvalue로 만듦
이후 위에 사용된 lvalue는 사용x

Rvalue 참조는 RValue가 아니다
int lvalue1;
int&& rvalueRef1 = lvalue1; // Error
int&& rvalueRef2 = std::move(lvalue1); // OK.
int&& rvalueRef3 = rvalueRef2; // Error.

복사
size_t length = strlen(other.name) + 1;
name = new char[length];
strcpy_s(name, length, other.name);

이동
==name = other.name;== (이동도 복사가 일어남) - >그래서 move는 const붙이면안됨
other.name = nullptr;


#### Perfect Forwarding
std::forward()
- std::forward()로 L-Value는 L-Value로 R-Value는 R-Value로 형변환할 수 있다.
- std::forward()는 특히 템플릿 프로그래밍에서 사용하면 유용하다.

## 정리

- 깊은 복사보다 얕은 복사가 더 빠르다.
- move는 얕은 복사와 메모리 이중 해제 방지 처리를 한다.
- 따라서 기본 복사보다는 move가 더 빠르다.
- move는 이후에 사용하지 않는 변수에 대해서 사용해야 한다.