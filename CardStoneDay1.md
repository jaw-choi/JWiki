 Day 1 — 2026-06-13 작업 요약
    CardStone 진행 현황 (Day 1~5 완료)

  Day 1 — 프로젝트 구조 & 데이터 설계

  - Unity URP 2D 프로젝트 생성, CS prefix + 폴더 구조 확립
  - 핵심 데이터 클래스 설계
    - CSCardData (ScriptableObject 에셋)
    - CSCardRuntimeData (런타임 HP/상태 관리)
    - CSTurnState enum, CSBattleStateMachine

  Day 2 — 필드 시스템 & 카드 에셋

  - CSFieldManager: 슬롯 3개, Queue<CSCardData> 덱, AutoDeploy, RemoveCard, IsDefeated
  - CSCardController: 카드 한 장 런타임 제어
  - ScriptableObject 카드 에셋 생성 (공격/방어/주술 타입)

  Day 3 — 전투 핵심 로직

  - CSCardEffectHandler: 카드 효과 실행 (HP 감소, Warlord 인접 데미지, Spell isUsed)
  - CSTurnManager: 플레이어/적 턴 전환
  - CSBattleManager: 전체 전투 루프 오케스트레이션
  - 버그 발견·수정: FieldCards[0] 하드코딩 → FindFirstCard() 반복 탐색으로 수정
  - DevLog/Errors.md 생성 (논리적 오류 기록 시스템)

  Day 4 — 적 AI + 완전한 턴 루프

  - CSEnemyAI (pure class, not MonoBehaviour): 랜덤 공격자/대상 선택
  - ExecuteEnemyTurn() → 플레이어 공격 → 사망 처리 → 적 공격 → 사망 처리 → 플레이어 턴 반복
  - ProcessDeaths() + CheckGameOver() 전투 루프 완성

  Day 5 — UI 구현

  - CSCardUI: 스프라이트 + HP 텍스트 표시, 하이라이트
  - CSBattleUI: Pointer.current 입력 (Mouse + 터치 통합), Physics2D.OverlapPoint 클릭 감지, 상태 기반 카드 선택 흐름
  - CSResultUI: 승리/패배 패널, 재시작 버튼
  - 버그 수정: New Input System 충돌 → Input.GetMouseButtonDown 사용 불가, Device Simulator는 터치 입력 → Pointer.current로 해결
  - 한글 폰트: 강원교육모두 Bold TMP Font Asset 적용

  ---
  생성된 파일

  CardStone/
  └── Assets/
      ├── Font/
      │   ├── 강원교육모두 Bold SDF.asset   ← TMP 한글 폰트 에셋
      │   └── 강원교육모두 Bold.ttf
      │
      ├── Prefabs/
      │   └── PFCard.prefab                 ← 카드 프리팹
      │
      ├── Scenes/
      │   └── SCBattle.unity
      │
      ├── ScriptableObjects/
      │   └── Cards/
      │       ├── CSCardDataNormal01~03.asset
      │       ├── CSCardDataWarlord01.asset
      │       ├── CSCardDataRanged01.asset
      │       ├── CSCardDataHealer01.asset
      │       └── CSCardDataSpell01.asset
      │
      ├── Scripts/
      │   ├── Battle/
      │   │   ├── CSBattleManager.cs        ← 전투 루프 오케스트레이션
      │   │   ├── CSBattleResolver.cs
      │   │   ├── CSCardEffectHandler.cs    ← 카드 효과 실행
      │   │   ├── CSEnemyAI.cs              ← 적 AI (pure class)
      │   │   ├── CSFieldManager.cs         ← 슬롯/덱 관리
      │   │   └── CSTurnManager.cs          ← 턴 전환
      │   ├── Card/
      │   │   ├── CSCardController.cs       ← 카드 런타임 제어
      │   │   ├── CSCardData.cs             ← ScriptableObject 에셋
      │   │   ├── CSCardRuntimeData.cs      ← 런타임 HP/상태
      │   │   └── CSCardType.cs             ← enum (Normal/Warlord/Ranged/Healer/Spell)
      │   ├── Core/
      │   │   ├── CSBattleStateMachine.cs   ← 상태 머신 + OnStateChanged 이벤트
      │   │   ├── CSGameManager.cs
      │   │   └── CSTurnState.cs            ← enum (PlayerSelectCard/Target/EnemyTurn/ApplyEffect/GameOver)
      │   ├── Debug/                        ← (비어 있음, CSInputTest 삭제됨)
      │   └── UI/
      │       ├── CSBattleUI.cs             ← 입력 감지, 카드 선택 흐름
      │       ├── CSCardUI.cs               ← 스프라이트·HP 표시, 하이라이트
      │       └── CSResultUI.cs             ← 게임오버 패널
      │
      └── Sprites/
          ├── Cards/
          │   ├── CARD_Normal_01~03.png
          │   ├── CARD_Warlord_01.png
          │   ├── CARD_Ranged_01.png
          │   ├── CARD_Healer_01.png
          │   └── CARD_Spell_01.png
          └── UI/                           ← (비어 있음)


  ---
  결정 사항

  ┌────────────────┬─────────────────────────────────────────────────────┐
  │      항목      │                        결정                         │
  ├────────────────┼─────────────────────────────────────────────────────┤
  │ 폴더 네이밍    │ 언더스코어 없음 (Scripts not _Scripts)              │
  ├────────────────┼─────────────────────────────────────────────────────┤
  │ 클래스 접두사  │ CS + PascalCase (CSBattleManager)                   │
  ├────────────────┼─────────────────────────────────────────────────────┤
  │ 카드 타입      │ Normal / Ranged / Warlord / Healer / Spell          │
  ├────────────────┼─────────────────────────────────────────────────────┤
  │ 데이터 구조    │ CSCardData (고정) + CSCardRuntimeData (런타임) 분리 │
  ├────────────────┼─────────────────────────────────────────────────────┤
  │ 주술 생존 판정 │ HP 기준 아닌 isUsed 플래그로 별도 처리              │
  └────────────────┴─────────────────────────────────────────────────────┘
