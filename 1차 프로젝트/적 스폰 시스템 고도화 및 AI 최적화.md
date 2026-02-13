
   * 핵심 목표: 뱀파이어 서바이버즈 스타일의 웨이브 기반 적 스폰 시스템을 구현하고, A* 알고리즘의 시간 분산 처리를 위한 기반을 마련한다. culling을 이용해서 카메라 밖 물체는 Draw하지 않아서 최적화한다.
   * 구현 내용:
       1. `EnemySpawner` 확장:
           * GameLevel에 EnemySpawner 클래스를 도입합니다.
           * Config/Setting.txt 또는 새로운 데이터 파일(예: Assets/Stage1_Waves.txt)에서 웨이브 데이터를 로드하도록 구현합니다. 데이터는 시간, 스폰될 적의
             종류, 수량 등을 포함할 수 있습니다.
           * EnemySpawner는 GameLevel의 Update에서 현재 게임 시간을 기준으로 웨이브 데이터를 참조하여 적들을 플레이어의 화면 밖(경계)에 스폰합니다.
       2. `PathfindingManager` 구현:
           * Engine/Core 또는 Game/Util에 PathfindingManager.h/PathfindingManager.cpp를 추가합니다.
           * 이 매니저는 std::queue<Enemy*> 또는 std::vector<std::pair<Enemy*, int>>와 같은 자료구조를 사용하여 길찾기 요청을 관리합니다.
           * RequestPath(Enemy* enemy) 메서드를 구현하여 적이 길찾기를 요청할 때 큐에 추가합니다.
           * Update() 메서드를 구현하여 매 프레임 큐에서 소수의 적(예: 5~10마리)을 꺼내어 길찾기(아직은 플레이어 방향으로의 단순 이동 로직)를 수행하고,
             결과를 해당 적에게 업데이트합니다.
       3. `Enemy` AI에 통합:
           * Enemy 클래스에 PathfindingManager 인스턴스를 전달받거나 접근할 수 있도록 합니다.
           * Enemy::Update에서 자신의 경로가 없거나, 일정 시간(예: 1초)마다 PathfindingManager.RequestPath(this)를 호출하도록 합니다.
   * 테스트:
       * 시간이 지남에 따라 적들이 웨이브 형태로 스폰되는지 확인.
       * PathfindingManager의 큐에 적들이 쌓이고, 매 프레임 일정 수의 적들만 처리되는지 디버그 메시지를 통해 확인.
       * 적들이 스폰 지점에서 플레이어 방향으로 이동하는지 확인.
   * 위기와 해결:
       * 위기(Problem): EnemySpawner가 적을 너무 많이 스폰하거나, 잘못된 위치에 스폰하여 게임 플레이를 방해하거나 충돌이 발생한다. PathfindingManager의 시간
         분산 로직이 제대로 작동하지 않아 여전히 프레임 드랍이 발생한다.
       * 해결(Solution): EnemySpawner의 웨이브 데이터 설정을 세심하게 조정하고, 스폰 위치가 항상 플레이어의 화면 밖에 있는지 확인하는 디버그 시각화를
         추가합니다. PathfindingManager에서는 한 번에 처리하는 적의 수를 조절하며, 각 적이 경로를 요청하는 주기를 다르게 설정하여 부하를 분산시킵니다. 실제
         A* 알고리즘 자체는 다음 단계에서 구현하고, 이 단계에서는 시간 분산 메커니즘의 안정성에 집중합니다.