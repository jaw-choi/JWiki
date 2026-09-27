### 1. 핵심 정리

전형은 서류 → AI면접 → AI활용 역량평가 → 직군면접 → 팀면접 순이고, 역량평가는 10월 3일 토요일 오후에 서류와 AI면접 합격자만 봅니다. 보내주신 정리본에 빠진 가장 중요한 조건이 하나 있는데, 넥슨이 별도로 제공하는 프로그램 환경 안의 AI만 쓸 수 있고, 테스트 화면을 벗어나 외부 도구를 쓸 수 없습니다. 평소 쓰던 Claude나 ChatGPT가 아니라 처음 보는 AI를 다뤄야 한다는 뜻이라, 특정 도구의 요령보다 어떤 AI에도 통하는 지시와 검증 습관이 중요합니다. [tistory](https://ideas21422.tistory.com/24)

공고에 적힌 평가 기준은 단순한 결과물이 아니라 문제 접근 방식, AI 활용의 효율성, 구조적 사고력입니다. 현직자들의 말도 같은 방향입니다. AI에 작업을 단순히 요청하는 것과 문제를 구체적으로 정의하고 결과가 의도와 맞는지 검증하는 것은 다른 역량이라는 점, 그리고 AI가 생성한 코드를 자기 실력으로 착각하기 쉬운데 면접에서 구조와 동작 원리를 물으면 기본기가 드러난다는 점입니다. 역량평가에서 제출한 코드는 이후 직군면접에서 질문 소재가 될 가능성이 높으니, 한 줄 한 줄 설명할 수 있는 코드만 제출한다는 원칙으로 연습하세요. [넥슨, 코딩테스트를 없앴다, 그럼 뭘 보나? — 넥슨 AI 채용 +2](https://ideas21422.tistory.com/24)

### 2. 연습 방식

제가 출제자라 정답을 알고 있으므로, 문제를 푸는 동안 쓸 AI는 이 대화가 아닌 **새 채팅 창**을 쓰세요. 실전처럼 낯선 환경을 원하면 다른 회사 AI를 써도 좋습니다. 제한 시간은 40분으로 잡고, 끝나면 아래 여섯 가지를 이 대화에 붙여 제출해 주세요.

1. 내가 이해한 문제 정의
2. 해결 순서 계획
3. AI와 나눈 대화 원문 (프롬프트 그대로)
4. 최종 수정 코드
5. 검증 방법과 결과
6. 남은 리스크나 확인 못 한 부분

채점은 문제 정의 20, 구조화 15, AI 활용 효율성 25, 검증 25, 결과물 15로 하고, 제출 코드는 제가 공개하지 않은 추가 테스트로 한 번 더 돌려보겠습니다. 피드백 후 바로 다음 문제를 드립니다.

### 3. 연습 문제 1: 버프 시스템 공격력 계산 오류

기획서 명세와 QA 리포트, 버그가 있는 코드, 테스트가 한 파일에 들어 있습니다. 현재 5개 테스트 중 4개가 FAIL이고, 수정 후에도 이미 통과하는 T3가 깨지면 안 됩니다. 제 쪽에서 컴파일해서 버그 재현과 풀이 가능 여부는 확인했습니다.

Presented file

빌드는 `g++ -std=c++17 -O0 -g problem1_buff_system.cpp -o p1 && ./p1` 이고, Visual Studio에서 빈 프로젝트에 붙여 넣어도 됩니다.

이후 문제는 실전에서 나올 법한 유형을 돌아가며 드릴 예정입니다. 로직 버그 수정(이번 문제), 오브젝트 풀의 댕글링 포인터 같은 메모리 문제, 전투 로그 CSV를 분석해 밸런스 이상 원인 찾기, 기존 인벤토리 코드에 새 기능 추가하기, 충돌 검사 성능 개선 순서입니다. 유형이 바뀌면 AI에게 맡길 부분과 직접 판단할 부분도 달라지니 그 차이를 익히는 게 목표입니다.

풀이를 제출하면 채점과 피드백을 드리겠습니다.
---

---
// =============================================================
// [연습 문제 1] 버프 시스템 공격력 계산 오류
// 빌드: g++ -std=c++17 -O0 -g problem1_buff_system.cpp -o p1 && ./p1
// =============================================================
//
// [기획서 명세]
//  1. 최종 공격력 = (기본 공격력 + 고정 증가량 합계) x (1 + 퍼센트 증가량 합계)
//     결과는 소수점 이하 버림(int)
//  2. 같은 id의 버프를 다시 받으면
//     - stackable == false : 새로 추가하지 않고 지속시간만 초기화
//     - stackable == true  : maxStacks까지 스택 증가, 지속시간 초기화
//       효과량 = value x stacks
//  3. Update(dt)마다 모든 버프의 남은 시간이 dt만큼 줄고
//     남은 시간이 0 이하가 되면 그 프레임에 제거
//
// [QA 리포트]
//  - "전사의 검(+20)을 두 번 먹으면 공격력이 140이 됩니다. 기획 의도는 120입니다."
//  - "버프를 여러 개 받으면 기획서 계산값보다 공격력이 높게 나옵니다.
//     버프를 받는 순서에 따라 값이 달라진다는 제보도 있습니다."
//  - "가끔 버프가 끝나야 할 시간보다 늦게 사라집니다. 재현이 매번 되지는 않습니다."
//
// [과제]
//  원인을 찾아 수정하고 아래 테스트가 모두 PASS 하도록 만드세요.
//  이미 PASS 하는 테스트가 깨지면 안 됩니다.
//  main()의 테스트 코드는 수정하지 마세요. (테스트 추가는 자유)
// =============================================================

#include <cstdio>
#include <string>
#include <vector>

enum class ModType { Flat, Percent };

struct BuffData {
    std::string id;
    ModType type;
    float value;      // Flat: 고정 수치, Percent: 0.25 == 25%
    float duration;   // 초
    bool stackable;
    int maxStacks;
};

struct ActiveBuff {
    BuffData data;
    float remaining;
    int stacks;
};

class Character {
public:
    explicit Character(int baseAttack) : baseAttack_(baseAttack) {}

    void ApplyBuff(const BuffData& data) {
        for (auto& b : buffs_) {
            if (b.data.id == data.id && b.data.stackable) {
                if (b.stacks < b.data.maxStacks) b.stacks++;
                b.remaining = data.duration;
                return;
            }
        }
        buffs_.push_back({data, data.duration, 1});
    }

    void Update(float dt) {
        for (size_t i = 0; i < buffs_.size(); ++i) {
            buffs_[i].remaining -= dt;
            if (buffs_[i].remaining <= 0.0f) {
                buffs_.erase(buffs_.begin() + i);
            }
        }
    }

    int GetAttack() const {
        float attack = static_cast<float>(baseAttack_);
        for (const auto& b : buffs_) {
            float amount = b.data.value * b.stacks;
            if (b.data.type == ModType::Flat) attack += amount;
            else attack *= (1.0f + amount);
        }
        return static_cast<int>(attack);
    }

    size_t BuffCount() const { return buffs_.size(); }

private:
    int baseAttack_;
    std::vector<ActiveBuff> buffs_;
};

// ---------------- 테스트 (수정 금지) ----------------
static int g_fail = 0;
static void Check(const char* name, long long expected, long long actual) {
    bool ok = expected == actual;
    if (!ok) g_fail++;
    std::printf("[%s] %-34s expected=%lld actual=%lld\n",
                ok ? "PASS" : "FAIL", name, expected, actual);
}

int main() {
    const BuffData sword    {"sword",    ModType::Flat,    20.0f, 10.0f, false, 1};
    const BuffData rage     {"rage",     ModType::Percent, 0.5f,  10.0f, false, 1};
    const BuffData blessing {"blessing", ModType::Percent, 0.25f, 10.0f, false, 1};
    const BuffData fury     {"fury",     ModType::Flat,    10.0f, 10.0f, true,  3};

    {   // T1: 여러 버프 합산 공식
        Character c(100);
        c.ApplyBuff(sword); c.ApplyBuff(rage); c.ApplyBuff(blessing);
        Check("T1 formula (flat+percent)", 210, c.GetAttack());
    }
    {   // T2: 비중첩 버프 재획득
        Character c(100);
        c.ApplyBuff(sword); c.ApplyBuff(sword);
        Check("T2 non-stackable refresh", 120, c.GetAttack());
    }
    {   // T3: 중첩 버프 최대 스택
        Character c(100);
        for (int i = 0; i < 5; ++i) c.ApplyBuff(fury);
        Check("T3 stackable max stacks", 130, c.GetAttack());
    }
    {   // T4: 동시 만료
        Character c(100);
        c.ApplyBuff({"a", ModType::Flat, 10.0f, 1.0f, false, 1});
        c.ApplyBuff({"b", ModType::Flat, 10.0f, 1.0f, false, 1});
        c.ApplyBuff({"c", ModType::Flat, 10.0f, 5.0f, false, 1});
        c.Update(1.0f);
        Check("T4 simultaneous expiry attack", 110, c.GetAttack());
        Check("T4 simultaneous expiry count", 1, (long long)c.BuffCount());
    }

    std::printf("\n%s (%d failed)\n", g_fail == 0 ? "ALL PASSED" : "SOME FAILED", g_fail);
    return g_fail == 0 ? 0 : 1;
}
