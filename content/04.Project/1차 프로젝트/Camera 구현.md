
1. 카메라와 월드(World) 개념 도입 (`Engine/Level/Level.h`)
       * 목표: 화면보다 더 큰 가상의 게임 공간("월드")을 정의하고, 그 공간의 특정 부분을 보여주는 "카메라"를 만듭니다.
       * 방법:
           * Level 클래스에 Vector2 worldSize; 멤버를 추가하여 레벨의 전체 크기(예: 160x30)를 정의합니다.
           * Level 클래스에 Vector2 cameraPosition; 멤버를 추가합니다. 이 좌표는 월드 공간에서 카메라가 현재 비추고 있는
             영역의 왼쪽 상단 모서리 위치를 의미합니다.


   2. 카메라 위치 업데이트 (`Game/Level/GameLevel.cpp`)
       * 목표: 매 프레임마다 플레이어의 위치에 맞춰 카메라의 위치를 갱신합니다.
       * 방법:
           * GameLevel의 Tick() 함수에서 플레이어의 위치가 업데이트된 후 다음 로직을 실행합니다.
           * 카메라 중심 맞추기: 카메라의 x 위치를 플레이어의 x위치 - (화면 너비 / 2)로 계산하여 플레이어가 화면 중앙에 오도록
             합니다.
           * 카메라 이동 제한: 카메라 위치가 worldSize를 벗어나지 않도록 좌표를 보정(Clamp)합니다. 예를 들어, 카메라의 x
             위치가 0보다 작아지거나, 월드 너비 - 화면 너비보다 커지지 않게 막습니다. 이렇게 하면 월드 밖의 빈 공간이 보이지
             않게 됩니다.


   3. 월드 좌표를 화면 좌표로 변환하여 그리기 (`Engine/Actor/Actor.cpp`)
       * 목표: 모든 게임 오브젝트(Actor)를 월드 좌표 기준이 아닌, 카메라에 보리는 화면 좌표 기준으로 그리도록 수정합니다.
       * 방법:
           * 모든 Actor의 Draw() 함수를 수정합니다.
           * Renderer에 그리기 요청(Submit)을 하기 직전에, 액터의 월드 위치에서 현재 Level의 cameraPosition을 뺍니다. 이
             결과가 실제 화면에 그려질 "화면 좌표"가 됩니다.
           * 계산식: Vector2 screenPosition = actor.position - level.cameraPosition;
           * Renderer::Get().Submit(image, screenPosition, ...) 와 같이 screenPosition을 사용해 렌더링합니다.


   4. 플레이어 이동 범위 확장 (`Game/Actor/Player.cpp`)
       * 목표: 플레이어가 화면 끝에 막히지 않고, 새로 정의한 worldSize 안에서 자유롭게 움직일 수 있도록 합니다.
       * 방법:
           * Player의 MoveLeft(), MoveRight() 함수에서 플레이어의 위치를 제한하던 코드를 수정합니다.
           * 기존에는 화면 너비(Engine::Get().GetWidth())를 기준으로 경계를 확인했지만, 이제는 GetOwner()->GetWorldSize().x를
             기준으로 월드 끝에 도달했는지 확인하도록 변경합니다.

  요약


  이 설계의 핵심은 게임 로직(위치, 이동)은 '월드 좌표계'에서 다루고, 그리기(Rendering) 직전에만 '카메라'를 이용해 '화면
  좌표계'로 변환하는 것입니다. 이렇게 역할을 분리하면 자연스러운 스크롤링 기능을 구현할 수 있습니다.
