────────────────────────────────

## High-Level Architecture (상위 아키텍처)

- GameManager.cs (4행)는 DontDestroyOnLoad 기반의 글로벌 세션 싱글톤으로, 점수 관리, 씬 전환, 플레이어/카메라 리셋, 결과 UI 제어를 담당합니다. 대부분의 스크립트는 GameManager의 존재를 전제로 작성되어 있습니다.
    
- UI/프레젠테이션 계층은 MainMenuManager.cs (5행), MenuManager.cs (4행) 등 지속 매니저를 사용해 씬별로 프리팹과 패널을 교체하지만, 전체 흐름 제어는 여전히 GameManager에 의존합니다.
    
- 오디오(AudioManager.cs (5행)), 설정(SettingsManager.cs (4행)) 같은 시스템도 싱글톤으로 씬에서 생성되며 여러 컴포넌트에서 직접 접근합니다. 이로 인해 시스템 간 통신은 대부분 static/global 방식입니다.
    
- 레벨 콘텐츠는 WorldScroller.cs (8행)가 런타임 중 프리팹 세그먼트를 관리하며 구성됩니다. FigmaPrefabMap.cs (4행) 및 에디터 변환 툴은 외부 파이프라인의 흔적을 보여주지만, 런타임에서는 직렬화된 리스트에 의존합니다.
    

────────────────────────────────

## Core Systems (핵심 시스템)

- 게임 세션 관리: 타이머, 점수 누적, 재시작/로드 흐름, UI 등록 처리 (GameManager.cs (33–210행)).
    
- 플레이어 엔티티:
    
    - Player.cs (3–119행): 시각 요소, 스케일 처리
        
    - PlayerController.cs (5–312행): 입력, 물리 처리  
        두 스크립트 모두 실패/클리어 이벤트를 GameManager에 직접 전달합니다.
        
- 카메라: ScoreBasedCameraFollow.cs (8–63행)에서 플레이어를 추적하며 점수에 따른 줌 아웃을 수행하고, 리셋 시 스냅 훅을 제공합니다.
    
- 배경 스트리밍: WorldScroller.cs가 세그먼트 순서, 셔플, 카메라 바운드 계산을 포함해 처리합니다 (58–186행).
    
- UI 컨트롤러: 결과 패널, 설정, 탭-투-스타트 오버레이, 네비 버튼 등은 각 패널을 캡슐화하지만 씬 이름과 GameManager 훅에 의존합니다.
    
- 오디오/설정:
    
    - AudioManager.cs (41–210행): 음악/SFX 라우팅, 믹서 연동, 오디오 소스 생성
        
    - SettingsManager.cs (31–86행): PlayerPrefs 기반 옵션 저장 및 믹서 값 적용
        

────────────────────────────────

## Gameplay Flow (게임플레이 흐름)

- 부팅 시 로고/메뉴 씬 로드 → MainMenuManager가 UI 프리팹 생성 → 버튼이 GameManager.Restart 또는 씬 로드를 호출합니다.
    
- 게임 씬 진입 시 GameManager.HandleSceneLoaded가 플레이어/카메라 캐시, 위치/물리 리셋, 점수 시작, 음악 재생을 처리합니다.
    
- 플레이어 이동:
    
    - PlayerController.Update/FixedUpdate: 클릭/터치 홀드 해석, 방향 플립, 눈 FX 생성, Rigidbody 속도 조정
        
    - Player.Update: 눈덩이 성장 및 화면 이탈 판정
        
- 패배 조건: 장애물 충돌 또는 뷰포트 이탈 → GameManager.GameOver
    
- 클리어 조건: FinishLine 트리거 → GameManager.LevelClear
    
- 무한 지형: WorldScroller.Update가 카메라 아래에서 세그먼트를 재활용합니다.
    

────────────────────────────────

## Code Quality Risks (코드 품질 리스크)

- 과도한 책임 집중:
    
    - GameManager는 점수, 씬 로딩, 오브젝트 풀링, UI 등록, 오디오 트리거까지 담당합니다.
        
    - PlayerController는 입력, 상태 로직, 물리, FX, 오디오를 한 파일에 혼합합니다.
        
- 강한 결합:
    
    - GameManager.Instance, AudioManager.instance가 항상 존재한다고 가정합니다.
        
    - FinishLine, UI 스크립트들이 GameManager를 직접 호출합니다.
        
- 로그/번역 잔여물:
    
    - PlayerController, SnowSprayController에 디버그 로그가 남아 있어 가독성과 성능에 악영향을 줍니다.
        

────────────────────────────────

## Unity Lifecycle 이슈

- PlayerController에 IsGameplayActive()가 정의되어 있으나 사용되지 않아, 게임 정지 상태에서도 입력/물리 로직이 계속 실행됩니다.
    
- AudioManager.Awake에서 Camera.main에 즉시 접근해, 카메라 초기화 이전에 null이 될 위험이 있습니다.
    
- GameManager.Awake에서 HandleSceneLoaded를 수동 호출해, 씬 오브젝트 초기화 이전에 FindObjectOfType을 실행할 수 있습니다.
    

────────────────────────────────

## Performance (성능)

- GC/로그 비용:
    
    - PlayerController.Update에서 문자열 포맷 Debug 로그 생성
        
    - SnowSprayController.FixedUpdate에서 매 프레임 로그 출력
        
- Update 비용:
    
    - Player.Update에서 매 프레임 Camera.main 조회 및 뷰포트 계산
        
    - WorldScroller.Update에서 카메라 프러스텀 계산 반복
        
- 오브젝트 생성:
    
    - AudioManager가 Awake에서 GameObject/AudioSource를 생성해 씬 재로드 시 중복 위험
        

────────────────────────────────

## Scalability & Data (확장성/데이터)

- 장애물/무기 추가 시 하드코딩된 태그와 스크립트 의존
    
- 씬 이름이 문자열 리터럴로 여러 스크립트에 분산
    
- WorldScroller는 데이터 기반 난이도 곡선 없이 수동 리스트에 의존
    
- FigmaPrefabMap은 런타임에서 활용되지 않아 정적 프리팹으로 고정됨
    

────────────────────────────────

## Testing (테스트)

- EditMode/PlayMode 테스트가 전혀 없음
    
- 고위험 시스템:
    
    - GameManager 세션 전환
        
    - PlayerController 플립 로직
        
    - WorldScroller 세그먼트 재활용
        
- 권장 테스트:
    
    1. 세션 라이프사이클 PlayMode 테스트
        
    2. 입력→이동 시뮬레이션 테스트
        
    3. 월드 스크롤링 통합 테스트
        
    4. UI 버튼/오디오 설정 회귀 테스트
        

────────────────────────────────

## Next 3 Refactor Targets (상위 3 리팩터링 대상)

1. GameManager  
    세션 상태, 플레이어 스폰, UI 제어를 분리해 전역 결합도를 낮추고, 신규 모드/멀티플레이 확장을 용이하게 합니다.
    
2. PlayerController  
    입력 해석과 물리 처리를 분리하고, 실제 게임플레이 상태에 따라 실행을 게이트하며, 플립 상태 머신을 캡슐화합니다.
    
3. Audio/Settings 스택  
    설정은 SettingsManager가 소유하고 AudioManager는 재생/풀링에 집중하도록 역할을 분리합니다. 카메라 바인딩을 안전하게 처리하고 이벤트 기반 연동으로 확장성을 확보합니다.
    

────────────────────────────────

## 다음 할 일 추천 (현실적인 우선순위)

### 1단계: “지금 안 고치면 계속 발목 잡는 것” (1주 이내)

- PlayerController.Update / FixedUpdate에 게임플레이 활성 상태 게이트 추가
    
- Debug.Log 전부 제거 또는 컴파일 타임 플래그로 비활성화
    
- Camera.main 접근을 캐싱 방식으로 전환
    

### 2단계: “구조 안정화” (1–2주)

- GameManager 분해 설계:
    
    - SessionService
        
    - SceneFlowController
        
    - UIFlowController
        
- 씬 이름을 ScriptableObject 또는 enum 기반 설정으로 중앙화
    

### 3단계: “확장 대비” (이후)

- WorldScroller 데이터화(난이도 곡선, 세그먼트 가중치)
    
- PlayerController 입력/물리 분리
    
- 최소 PlayMode 테스트 2–3개 도입(세션, 스크롤링)
    

### Obsidian 정리 권장

- 이 분석 전체를 Technical_Diagnosis.md로 저장
    
- Next 3 Refactor Targets를 Refactoring_Roadmap.md의 Phase 1 목표로 바로 연결
    
- PlayerController, GameManager 각각을 Phase_1.md의 개별 작업 노트로 분리
    

요약하면,  
지금 상태는 **게임은 잘 돌아가지만 구조적 부채가 명확히 보이는 단계**입니다.  
가장 좋은 선택은 기능 추가를 멈추고, 위 1단계 작업부터 정리하는 것입니다.