RunTime Type Information - 실시간 타입 정보 (c#의 GetType or as)
cpp는 typeid, const type_info형

https://resonant-exception-448.notion.site/C-RTTI-RTTI-2c07519ce7cb81529baff46d4ceb525c
cpp에서 발전 순서
문자열(느림) -> 
매크로(보기간편) -> 
숫자 및 (enum)(순수가상함수로 모든 상속 클래스에 GetType() 제작 강제) -> 
전역(static)메모리 주소 사용 -> 
캡슐화(bool Equals(const RTTI& rtti) const { return this == &rtti; } )
-> == 연산자 오버로딩을 구현해두면 보다 편하게 사용할 수 있다.
-> 단일 상속의 추가(상속 정보도 넣어둠-단일상속까지만)
->[[최종코드]]
![[Pasted image 20260128115748.png]]
위 내용 즉, static 변수에 대해서는 초기화를 전역에서 따로 한다는 내용용
응용( 위 헤더, 아래 cpp에 들어간다다)
![[Pasted image 20260128115835.png]]
- 문자열을 사용하는 부분은 제거
- 고유 숫자 값 할당을 위해 전역 메모리 주소 사용
    - 왜? → 같은 클래스 타입이 공유하는 고유 값이 필요해서.
- 단일 상속을 선언할 수 있는 매크로 작성
- 현재는 부모 계층 검색을 위해 재귀적 탐색 방법을 사용하고 있는데, 동적 배열이나 해시테이블을 사용해 캐싱을 적용하면 성능을 더 개선시킬 수 있음




매크로는 전처리기가 처리
#define  \ 쓰면 한줄이상 작성가능
예시)
#define RTTI(name) \
public: \ 
virtual const char* ClassName() const { return #name; }

[커스텀 RTTI ]
업에서는 메모리주소사용 주로함
정적클래스변수의 메모리주소이용
```c++
class GameEntity
{
public:
    static const RTTI rtti;

    virtual const RTTI& Rtti() const
    {
        return rtti;
    }

    // ...
};

const RTTI GameEntity::rtti("GameEntity");

class GamePlayer : public GameEntity
{
public:
    static const RTTI rtti;

    virtual const RTTI& Rtti() const
    {
        return rtti;
    }
};

const RTTI GamePlayer::rtti("GamePlayer");

```

    

- 1단계: 문자열 기반
    
    - GetTypeName() 같은 함수로 "Player", "Enemy" 반환.
        
    - 단순하지만 비교가 무겁고(문자열 비교), 상속 관계 판정 같은 확장은 더 복잡해짐.
        
- 2단계: enum 기반
    
    - enum class TypeId { Player, Enemy, ... } 형태로 숫자 비교.
        
    - 비교는 빠르지만 “유연한 확장/플러그인/모듈 간 타입 추가”에 제약이 생기기 쉬움.
        
- 3단계: 유일 포인터(주소) 기반
    
    - 타입마다 전역/정적 객체(또는 정적 멤버)의 “주소”를 타입 식별자로 사용.
        
    - 비교는 포인터(정수) 비교라 빠르고, 전역 유일성이 보장되는 구조로 만들면 충돌이 줄어듦.
        
    - 보통은 Equals/IsA 같은 함수로 캡슐화해서 “주소 비교”를 외부에 노출하지 않게 정리.
        
- 결론
    
    - 문자열(쉬움/느림) → enum(빠름/제약) → 주소(빠름/구조 설계 필요)로 발전시키는 사고 흐름 자체가 핵심입니다.
        
    - 언리얼은 이 방향을 “거대한 리플렉션 시스템”으로 풀어낸 사례라고 보면 정리가 깔끔해집니다(에디터, 직렬화, GC, 네트워크 리플리케이션, 블루프린트 등에서 타입 정보가 핵심 인프라).
복습 요망
