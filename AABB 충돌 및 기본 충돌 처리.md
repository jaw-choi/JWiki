
   * 핵심 목표: 모든 게임 객체에 Axis-Aligned Bounding Box (AABB)를 적용하고, 이를 이용한 기본적인 충돌 감지 로직을 구현한다. (쿼드트리 통합 전)
   * 구현 내용:
       1. AABB 구조체/클래스 구현:
           * Engine/Math에 AABB.h를 추가하고, Vector2 min, Vector2 max 또는 Vector2 center, Vector2 halfSize를 포함하는 AABB 구조체/클래스를 정의합니다.
           * 두 AABB 간의 충돌 여부를 판별하는 Intersects(const AABB& other) 메서드를 구현합니다.
       2. `Actor`에 AABB 추가:
           * Actor 클래스에 AABB GetBoundingBox() const 가상 함수를 추가합니다.
           * Player, Enemy, PlayerBullet, EnemyBullet 등 각 Actor 파생 클래스에서 자신의 크기와 위치를 기반으로 정확한 AABB를 반환하도록 이 함수를
             오버라이드(override)합니다.
       3. 기본 충돌 감지 로직:
           * GameLevel의 Update 루프에서, PlayerBullet와 Enemy 간의 충돌을 모든 총알과 모든 적을 일일이 검사하는 방식으로 구현해봅니다. (나중에 쿼드트리로
             최적화할 것이지만, 현재는 AABB의 정확성 확인에 중점)
           * 충돌 발생 시, 양쪽 객체를 inactive 상태로 전환하거나 (총알), 체력을 감소시킵니다 (적).
   * 테스트:
       * 총알이 적에게 정확히 닿았을 때만 충돌이 감지되는지 확인.
       * 충돌 감지 후 총알과 적이 예상대로 처리(사라지거나 체력 감소)되는지 확인.
   * 위기와 해결:
       * 위기(Problem): AABB 크기나 위치 계산이 잘못되어 충돌이 너무 빨리 감지되거나 (Hitbox가 너무 큼), 아예 감지되지 않는다 (Hitbox가 너무 작음).
       * 해결(Solution): 각 Actor의 GetBoundingBox() 함수에서 반환되는 AABB의 크기와 위치를 디버그 모드에서 시각적으로 확인하거나, 콘솔에 AABB의 좌표값을
         출력하여 정확한지 검증합니다.
