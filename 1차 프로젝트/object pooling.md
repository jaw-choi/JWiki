BeginPlay활용 -> PreWarm(미리 할당하는 단계)
			-> 할당 시 몇개를 미리 할당할 것인가?
			-> 이유는? 기준은? 최적화가 되나?
			


![[Pasted image 20260210143054.png]]

매 프레임 삭제한다
delete 하면 actor의 destructor가 불리게 되고 actor는 safeDelete등이 실행된다.

player의 bullet, enemy 등은 게임이 지속되는 동안 계속 생성된다.

그럼 메모리는 계속 생성,해제(new,delete)를 반복한다.

1. 이에 object pool을 사용하여 메모리 단편화를 줄일 수 있다.

2. delete 자체의 비용이 크다.


3. **pool을 해당 객체 포인터 타입의 static 벡터로 둔 이유**
    - **타입별로 다른 초기화/리셋 로직**이 필요합니다.  
        PlayerBullet, Enemy, ExpGem은 생성자 인자, 상태 초기화가 서로 다르기 때문에 **타입 전용 풀**이 가장 단순하고 안전합니다.
    - static으로 둔 이유는 **해당 클래스가 공유하는 풀**을 만들기 위해서입니다.  
        인스턴스마다 풀을 갖게 하면 재사용 자체가 의미가 없어집니다.
4. **왜 Actor* 하나로 통합 풀을 안 만들었나?**
    - Actor* 풀은 **다형성 기반 공용 풀**인데, 그러면 다음 문제가 생깁니다.
        - 꺼낼 때 실제 타입을 확인하고 안전하게 캐스팅해야 함
        - Initialize가 타입마다 다르므로 공통 인터페이스가 없으면 분기지옥
        - 실수로 다른 타입을 꺼내서 쓰면 버그/크래시 위험
    - 즉, **단순성과 안전성을 위해 타입별 풀**을 쓴 겁니다.
5. **Acquire와 Prewarm의 역할, 차이**
    - Prewarm(count)
        - **처음에 미리 N개를 생성해서 pool에 넣어둠**
        - 목적: 런타임 중 new가 튀지 않게 하여 **할당 비용/단편화 완화**
    - [Acquire(...)](https://file+.vscode-resource.vscode-cdn.net/c%3A/Users/user/.vscode/extensions/openai.chatgpt-0.4.71-win32-x64/webview/# "Acquire(...)")
        - pool에서 꺼내서 **재활성화하고 초기화**
        - pool이 비어 있으면 **새로 생성**(현재 구현 기준)
6. **GameLevel에서 prewarm count를 정한 기준?**
    - 현재 값은 **임의 추정치**입니다.  
        예) PlayerBullet 200, Enemy 50, ExpGem 150
    - 실제로는 아래 기준으로 조정하는 게 정석입니다.
        - 최대 동시 발사 수 / 생성 속도
        - 평균 화면 동시 존재 수
        - 플레이 테스트로 측정한 “최대치 + 여유분(10~30%)”
7. **count를 넘으면 어떻게 되나?**

- 지금 구현은 **pool이 비면 새로 new로 생성합니다.**  
    즉, **완전 고정 풀은 아닙니다.**
- 완전 고정 풀로 하고 싶다면  
    Acquire에서 pool이 비면 return nullptr; 하도록 바꾸면 됩니다.