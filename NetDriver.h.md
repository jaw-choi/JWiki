# 언리얼 네트워크 구조 요약

## 1. NetDriver / NetConnection / Channel 관계

언리얼 네트워크는 크게 **NetDriver → NetConnection → Channel** 구조로 이해하면 됩니다.

### ✅ NetDriver

`UNetDriver`는 네트워크 전체를 관리하는 중심 객체입니다.

대표 종류는 다음과 같습니다.

|종류|역할|
|---|---|
|Game NetDriver|일반적인 게임 네트워크 통신 담당|
|Demo NetDriver|리플레이 녹화/재생 담당|
|Beacon NetDriver|일반 게임플레이 외부 통신 담당|

서버에서는 여러 클라이언트의 연결을 관리하고, 클라이언트에서는 서버와의 연결을 관리합니다.

---

### ✅ NetConnection

`UNetConnection`은 **하나의 연결된 대상**을 의미합니다.

예를 들어:

|상황|NetConnection 의미|
|---|---|
|서버|접속한 각 플레이어 1명당 NetConnection 1개|
|클라이언트|서버와 연결된 NetConnection 1개|

즉, 서버는 여러 개의 `ClientConnections`를 갖고, 클라이언트는 보통 하나의 `ServerConnection`을 갖습니다.

---

### ✅ Channel

`Channel`은 실제 데이터를 주고받는 세부 통로입니다.

NetConnection 하나 안에는 여러 Channel이 존재할 수 있습니다.

주요 Channel은 다음과 같습니다.

|Channel 종류|역할|
|---|---|
|Control Channel|접속 상태, 종료, 핸드셰이크 같은 제어 메시지|
|Voice Channel|음성 데이터 전송|
|Actor Channel|서버에서 클라이언트로 복제되는 Actor마다 생성|

특히 **Actor Replication**은 대부분 `Actor Channel`을 통해 이루어집니다.

---

# 2. 서버와 클라이언트 접속 흐름

## 서버 시작 흐름

서버가 맵을 로드하면 대략 다음 흐름이 진행됩니다.

```
UEngine::LoadMap→ UWorld::Listen→ Game NetDriver 생성→ UNetDriver::InitListen→ IP / Port 바인딩→ 클라이언트 접속 대기
```

즉, 서버는 `Listen` 상태가 되면 클라이언트 연결을 받을 준비가 끝납니다.

---

## 클라이언트 접속 흐름

클라이언트가 서버에 접속하려고 하면 다음 흐름이 진행됩니다.

```
UEngine::Browse→ UPendingNetGame 생성→ InitNetDriver→ 서버용 UNetConnection 생성→ 서버로 데이터 전송 시작→ 핸드셰이크 진행
```

여기서 `UPendingNetGame`은 아직 게임 월드에 완전히 입장하기 전, 서버 접속을 준비하는 임시 상태라고 보면 됩니다.

---

# 3. 패킷 수신 처리 흐름

서버와 클라이언트 모두 `UNetDriver::TickDispatch`에서 네트워크 데이터를 받습니다.

패킷을 받으면 먼저 보낸 주소를 확인합니다.

```
패킷 수신→ 보낸 주소 확인→ 이미 연결된 주소인가?    → 예: 해당 NetConnection으로 전달    → 아니오: connectionless 패킷으로 보고 핸드셰이크 시작
```

이미 연결된 주소라면:

```
UNetConnection::ReceivedRawPacket
```

으로 넘겨 처리합니다.

연결되지 않은 주소라면 `StatelessConnectionHandlerComponent` 쪽에서 초기 핸드셰이크를 처리합니다.

---

# 4. 게임 레벨 핸드셰이크 흐름

NetDriver / NetConnection 레벨의 기본 연결이 끝나면, 실제 게임 입장을 위한 제어 메시지 흐름이 시작됩니다.

핵심 순서는 다음과 같습니다.

```
Client → Server : NMT_HelloServer → Client : NMT_ChallengeClient → Server : NMT_LoginServer : PreLogin 검사Server → Client : NMT_WelcomeClient → Server : NMT_NetSpeedServer : NetSpeed 조정접속 완료
```

각 단계 의미는 다음과 같습니다.

|단계|의미|
|---|---|
|NMT_Hello|클라이언트가 서버에 첫 인사|
|NMT_Challenge|서버가 검증용 challenge 전송|
|NMT_Login|클라이언트가 로그인 정보/응답 전송|
|PreLogin|서버 GameMode에서 접속 가능 여부 검사|
|NMT_Welcome|서버가 맵 정보와 입장 허가 전달|
|NMT_NetSpeed|클라이언트의 네트워크 속도 정보 전달|

즉, 단순히 소켓 연결만 되었다고 게임에 들어간 것이 아니라, **Control Message 기반의 게임 입장 절차**가 따로 있습니다.

---

# 5. 데이터 전송 구조: Packet과 Bunch

언리얼 네트워크 데이터는 크게 **Packet**과 **Bunch**로 나뉩니다.

## ✅ Packet

`Packet`은 NetConnection 사이에서 주고받는 네트워크 데이터 덩어리입니다.

패킷에는 다음이 들어갑니다.

```
Packet├─ Header 정보├─ ACK 정보└─ Bunch 0개 이상
```

---

## ✅ Bunch

`Bunch`는 Channel 사이에서 주고받는 실제 게임 데이터 단위입니다.

즉:

```
NetConnection끼리는 Packet을 주고받고,Channel끼리는 Bunch를 주고받는다.
```

라고 이해하면 됩니다.

---

# 6. RPC 전송 예시

예를 들어 클라이언트가 서버 RPC를 호출하면 다음 흐름이 됩니다.

```
Client에서 Server_RPC 호출→ 해당 Actor의 Actor Channel로 전달→ RPC ID와 파라미터를 Bunch로 직렬화→ NetConnection이 Bunch를 Packet에 담음→ 서버로 Packet 전송→ 서버 NetDriver가 Packet 수신→ 주소를 보고 NetConnection 찾음→ Packet을 Bunch로 분해→ Channel ID를 보고 Actor Channel로 전달→ Actor Channel이 RPC ID와 파라미터 해석→ 서버 Actor의 함수 실행
```

핵심은 RPC가 바로 함수 호출처럼 보이지만, 실제 내부에서는:

```
RPC 호출 → Bunch 생성 → Packet 전송 → 수신 후 Bunch 해석 → 함수 실행
```

흐름이라는 점입니다.

---

# 7. Reliable / Unreliable 개념

언리얼은 기본 네트워크 프로토콜이 항상 신뢰성을 보장한다고 가정하지 않습니다. 그래서 자체적으로 신뢰성 처리를 합니다.

## Reliable Bunch

`Reliable`로 표시된 Bunch는 유실되면 재전송됩니다.

```
Reliable Bunch 전송→ ACK 받을 때까지 보관→ 해당 Packet이 NAK 처리되면 Bunch 재전송→ ACK 확인되면 보관 목록에서 제거
```

---

## Unreliable Bunch

`Unreliable` Bunch는 유실되어도 재전송하지 않습니다.

예시로 적합한 데이터:

|데이터|이유|
|---|---|
|자주 갱신되는 위치 정보|다음 프레임에 새 정보가 또 옴|
|단발성 이펙트 중 중요도 낮은 것|놓쳐도 게임 진행에 큰 영향 없음|
|임시 상태 표시|최신 상태만 중요|

반대로 아이템 획득, 퀘스트 완료, 체력 감소 같은 중요한 데이터는 Reliable 성격이 필요합니다.

---

# 8. Packet Number와 Bunch Number

언리얼은 데이터 순서와 유실 여부를 확인하기 위해 번호를 붙입니다.

|번호|단위|특징|
|---|---|---|
|Packet Number|NetConnection 단위|모든 패킷마다 증가|
|Bunch Number|Channel 단위|Reliable Bunch마다 증가|

중요한 차이는 이것입니다.

```
Packet은 같은 번호로 재전송하지 않는다.Reliable Bunch는 같은 Bunch Number로 재전송될 수 있다.
```

즉, 유실된 데이터는 **기존 Packet을 다시 보내는 것이 아니라**, Reliable Bunch를 새 Packet에 다시 담아 보내는 방식입니다.

---

# 9. 패킷 유실 감지

수신자는 Packet Number 차이를 보고 유실을 판단합니다.

예를 들어 마지막으로 받은 패킷이 10번인데, 다음에 11번을 받으면 정상입니다.

```
현재 패킷 번호 - 마지막 성공 패킷 번호 = 1→ 정상
```

그런데 13번을 받으면:

```
13 - 10 = 3→ 11, 12번 패킷이 유실된 것으로 판단
```

0 이하라면:

```
이미 받은 패킷이거나순서가 뒤바뀐 패킷이거나외부에서 이상한 데이터를 보낸 것
```

으로 보고 보통 무시합니다.

---

# 10. ACK / NAK 처리

## ACK

수신자가 패킷을 정상적으로 받으면 송신자에게 ACK를 보냅니다.

```
“이 패킷 번호는 정상적으로 받았다”
```

라는 의미입니다.

## NAK

ACK 흐름 중 중간 번호가 비어 있으면, 송신자는 해당 패킷이 정상 수신되지 않았다고 판단합니다.

```
ACK: 10, 11, 14→ 12, 13은 NAK로 간주
```

이후 송신자는 그 패킷에 들어 있던 **Reliable Bunch**를 다시 보냅니다.

---

# 11. Partial Bunch

Bunch가 너무 크면 하나의 Packet에 다 들어가지 못할 수 있습니다.

이때 언리얼은 Bunch를 여러 조각으로 나눕니다.

```
PartialInitialPartialPartialFinal
```

수신 쪽에서는 이 조각들을 다시 합쳐 원래 Bunch로 복원합니다.

중요한 점은, Partial Bunch 중 하나라도 유실되면 전체 Bunch 재전송이 발생할 수 있다는 것입니다.

---

# 12. 연결 끊김과 복구

게임 중 연결이 끊길 수 있습니다.

예시:

```
인터넷 끊김와이파이 ↔ LTE 전환클라이언트 종료타임아웃IP/Port 변경
```

서버가 끊김을 인지하면 `UNetConnection`을 닫고 게임에 알립니다.

일시적인 끊김이고 서버가 아직 인지하지 못한 경우에는 패킷 손실이나 렉이 발생하지만, 자동 복구될 수도 있습니다.

만약 클라이언트의 IP나 Port가 바뀌면, 게임 코드에 알리지 않고 low-level handshake를 다시 수행해 복구를 시도할 수 있습니다.

---

# 13. 패킷 시뮬레이션 설정

코드에는 네트워크 테스트용 설정도 포함되어 있습니다.

대표 값은 다음과 같습니다.

|설정|의미|
|---|---|
|PktLoss|패킷 손실률|
|PktDup|패킷 중복|
|PktLag|지연 시간|
|PktLagVariance|지연 시간 변동폭|
|PktOrder|패킷 순서 뒤섞기|
|PktIncomingLoss|수신 패킷 손실|
|PktJitter|지터, 즉 불규칙한 지연|
|PktFrameDelay|송신 패킷 프레임 지연|
|PktIncomingFrameDelay|수신 패킷 처리 프레임 지연|

이 설정들은 멀티플레이 환경에서 렉, 패킷 유실, 순서 뒤바뀜 같은 상황을 테스트할 때 사용됩니다.

---

# 한 줄 핵심 정리

```
NetDriver는 네트워크 전체 관리자,NetConnection은 연결된 대상,Channel은 실제 데이터 통로,Packet은 연결 단위 데이터,Bunch는 채널 단위 게임 데이터입니다.
```

그리고 RPC나 Actor Replication은 내부적으로:

```
Actor / RPC 데이터→ Bunch→ Packet→ NetDriver 전송→ NetConnection 수신→ Channel 라우팅→ Actor 처리
```

흐름으로 동작합니다.

# 공부할 때 우선순위

처음 공부할 때는 아래 순서로 잡으면 이해가 쉽습니다.

1. **NetDriver / NetConnection / Channel 관계**
2. **서버 Listen과 클라이언트 Join 흐름**
3. **Handshake: Hello → Challenge → Login → Welcome**
4. **Packet과 Bunch 차이**
5. **RPC가 실제로 전송되는 과정**
6. **Reliable / Unreliable 차이**
7. **ACK / NAK / 재전송 구조**
8. **Actor Replication과 Actor Channel 연결**

이 파일은 언리얼 네트워크의 “큰 구조”를 설명하는 주석이 많아서, 처음에는 코드 멤버변수보다 위의 개념 흐름부터 잡는 것이 좋습니다.