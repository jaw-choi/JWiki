UDataTable, UDataAsset, 커스텀 컴포넌트를 활용하면 충분히 데이터 주도적인 설계 가능  
GAS를 쓰는 이유는?  
1. 기존 방식의 한계 -> 기본 스탯에 버프와 디버프가 중첩될 떄의 연산 순서를 직접 구현해야함  
- 특정 스탯이 변했을 때, UI나 다른 액터에 알려주는 델리게이트를 일일이 구조화해야 함  
- 프로젝트가 커질수록 개발자마다 스탯을 처리하는 방식이 달라져 유지보수와 최적화가 어려워짐  
2. GAS의 강점 -> 표준화된 프레임워크  
- 누가 코드를 짜든 정해진 규격(AttributeSet, GameplayEffect) 안에서 움직이게 되므로 팀원간의 구현의도를 파악하기 쉬움  
- 유연한 유지보수가 가능해짐  
3. GAS가 네트워크 처리를 쉽게 만드는 3가지 핵심 기능  
- 자동화된 스탯 및 태그 동기화  
- 기존 : 체력 변수를 Replicate 하려면 GetLifetimeReplicatedProps 함수를 오버라이딩하고, DOREPLIFETIME 매크로를 일일이 등록해야함  
- GAS : UAttributeSet에 선언된 스탯과 캐릭터가 가진 GameplayTag는 AbilitySystemComponent가 알아서 서버에서 클라이언트로 완벽하게 동기화  
- 복잡한 RPC의 캡슐화  
- 기존 : 타격 애니메이션을 멀티플레이이에서 재생 -> 클라이언트가 서버에 요청 (Server RPC) -> 서버가 모든 클라이언트에게 재생 명령을 내리는 코드를 매번 짜야함  
- GAS : AbilityTask_PlayMontageAndWait 실행 -> 내부적으로 필요한 RPC 통신을 알아서 처리 -> 모든 플레이어 화면에서 애니메이션이 동일하게 재생됨  
  
- 클라이언트 예측  
- 기존 : 핑이 높은 환경에서 클라이언트가 공격 버튼을 누르면, 서버의 허락이 떨어질 때까지 캐릭터가 가만히 멍을 때리는 '입력 지연'이 발생함  
- GAS : 클라이언트는 서버의 응답을 기다리지 않고 먼저 스킬 애니메이션 재생 마나 깎아버림 (예측) -> 이 후, 서버가 올바른 요청인지 검증하고 해킹이나 오류로 판명되면 클라이언트의 상태를 원래대로 강제 복구(Rollback) 시킴  
  
GAS 정리  
  
GA 사용  
1. Attack  
- 기존의 사용  
- Enhanced InputSystem Attack() 함수 바인딩  
- void Attack() 함수 호출  
- Attack() 애니메이션 + 판정 도구 + Check + 태그 값을 가져옴 + ApplyDamage시킴  
  
- GAS Attack  
- Enhanced InputSystem Attack() 함수 바인딩  
- void Attack() 함수 호출  
- Attack() 함수 안에 클래스가 가지고 있는 AbilitySystemComponent를 가져옴  
- TryActivateAbilityByTag로 호출함  
- GameAbility로 들어감  
- ActivateAbility 함수 실행  
- Montage_Play 로 AM_Attack 실행  
- AnimNotify -> GA_AttackHitCheck실행  
  
2. AttackHitCheck  
- 기존의 사용  
- AnimNotify 발생  
- 캐릭터나 무기 클래스에 있는 AttackHitCheck 직접 호출  
- 충돌 검사 -> 데미지 전달(ApplyDamage)  
- TakeDamage 처리  
  
- GAS AttackHitCheck  
- GameplayEvent Notify 발생 -> 몽타주 타격 시점에 일반 Notify가 아닌 Send Gameplay Event Notify 배치 (ex. Event.Character.AttackHitcheck)  
- AbilityTask 대기 : GA_Attack 내부 (Montage Play + AbilityTask_WaitGameplayEvent를 실행)  
- 이벤트 수신 및 판정 : Notify가 이벤틑를 쏘면 기다리던 Task가 이를 수신하여 연결된 HitCheck 로직을 실행함  
- AbilityTask_WaitTargetData를 사용해 판정결과를 가져오는 방식도 많이 쓰임  
- GameplayEffect 적용 : 맞은 대상의 AbilitySystemComponent를 가져옴. 기존의 ApplyDamage 대신 대미지 공식과 속성(Attribute) 변경 정보를 담고 있는 GameplayEffect(ex. GE_AttackDamage)를 Target ASC에 적용 (ApplyGameplayEffectToTarget) 시킴  
- Attribute 변경 : 대상의 ASC가 GE를 받아들여, 자체적으로 AttributeSet에 있는 체력(Health) 값을 규칙에 맞게 깎음  
  
3. Damage & Attribute(데미지와 스탯 관리)  
- 기존의 사용  
- TakeDamage 호출 : ApplyDamage를 통해 전달 받은 데미지를 AActor::TakeDamage() 함수를 오버라이딩하여 받음  
- 데미지 연산 : HP -= (Damage - Armor)  
- 스탯 변수 관리 : float HP / float MaxHP 등의 일반 션수 값을 직접 수정  
- 사망 판정 및 후처리 : 값이 수정된 후 HP가 0 이하인지 체크하는 if문을 작성 -> 캐릭터 Die() 함수 등을 호출  
- UI 업데이트 : 갱신된 HP 수치를 HUD에 반영하기 위해 델리게이트를 수동으로 Broadcast or UI 갱신 함수 직접 호출  
  
- GAS 사용  
- Gameplay Effect 적용 : 사전에 에디터에서 만들어둔 GE_Damage 에셋을 타겟의 ASC에 Apply함.  
- 어떤 스탯을 얼마나 깎을 지 -> 데이터 형식으로 정의  
- AttributeSet에서 스탯 관리 : 일반 float 변수 대신 UAttributeSet을 상속받은 전용 클래스에서 FGameplayAttributeData Health 형태로 마나, 방어력 등을 모아서 관리  
- PostGameplayEffectExecute 처리 : GE를 통해 최종 계산된 데미지가 들어오면, AttributeSet의 PostGameplayEffectExecute 함수가 콜백으로 반응함 -> 여기서 실제 Health 값을 깎고 값이 0이하가 되면 캐릭터에게 사망용 Tag(State.Character.Dead 등)을 부여하여 이벤트를 발생시킴  
- 자동화된 UI 업데이트 : ASC의 특정 Attribute가 변할 때, 발생하는 내장 델리게이트에 바인딩 -> 스텟 데이터가 변하면 코드 호출 없이도 자동으로 UI가 갱신됨