파일 IO
버퍼 : 메모리안 데이터 덩어리
1.File open
- 파일 읽고 쓰기 추가하기(append)
- stream 으로 처리
- 내부버퍼 필요
- 파일 위치 초기화
- fopen_s()
- r,w,a,r+,w+,a+
- EOF= End of File
- rt,wb,r+b
2.File close
열려있으면 다른곳에서는 접근권한없음
파일 입출력은 stream으로 처리
- fclose


```c++
#include <iostream>
int main() 
{
 FILE* file = nullptr; 
fopen_s(&file, "Test.txt", "rt"); 
if (file != nullptr) 
{
 char buffer[256] = { }; 
fseek(file, 24, SEEK_SET); 
while (!feof(file)) 
{
 fgets(buffer, 256, file); 
std::cout << buffer; 
 } 
 fclose(file); 
 } 
}
```
임의접근(File Position)
3. fseek : FP이동하기
4. ftell : FP의 현재 위치 반환
5. rewind : 처음으로 되돌릴때

예제
```c++
#include <iostream>
 int main()
  { 
  const char* message = "C 표준 라이브러리 함수로 생성한 텍스트 파일입니다.\n"; 
  FILE* file = nullptr;
   fopen_s(&file, "Test.txt", "wt");//wt(write),rt(read),rb(read binary)
    if (file == nullptr) 
    { 
    std::cout << "Failed to open file.\n"; 
    __debugbreak(); 
    } 
    
    fputs(message, file);
    fclose(file);
  }
```



2. C 파일 모드(기본 3계열)와 차이
    

- r : 읽기(파일 없으면 실패)
    
- w : 쓰기(기존 내용 삭제/덮어쓰기, 파일 없으면 생성)
    
- a : 추가(항상 파일 끝에 붙임, 파일 없으면 생성)
    
- - : 읽기/쓰기를 둘 다 가능하게 하는 확장
        
    
    - r+ : 읽기 기반 + 쓰기 가능(파일 없으면 실패)
        
    - w+ : 쓰기 기반 + 읽기 가능(파일 없으면 생성, 기존 내용 삭제)
        
    - a+ : 추가 기반 + 읽기 가능(파일 없으면 생성, 쓰기는 항상 끝에 붙음)
        
- 핵심 차이 한 줄 요약
    
    - w는 “처음부터 다시 쓰기(리셋)”
        
    - a는 “끝에 이어붙이기(로그/누적)”
        
    - w로 열고 fseek로 끝으로 보내서 붙일 수도 있지만, a는 그 편의 기능이 모드로 박혀 있는 것
        

3. 텍스트 모드 vs 바이너리 모드
    

- 텍스트 모드
    
    - 줄바꿈 변환 같은 “편의 변환”이 들어갈 수 있음(대표: 윈도우 CRLF ↔ 내부 처리 LF)
        
    - 일부 환경에선 EOF 처리(컨트롤-Z 등) 같은 레거시 관습이 얽혀 있을 수 있음
        
    - 사람 눈으로 읽는 텍스트를 다룰 때 편합니다.
        
- 바이너리 모드
    
    - 바이트를 “있는 그대로” 읽고 씁니다(==변환 없음==).
        
    - 이미지/사운드/직렬화 데이터/네트워크 패킷/커스텀 포맷 등은 무조건 바이너리로 보는 편이 안전합니다.
        
- 중요한 관점
    
    - char[256] 버퍼는 “문자열”이 아니라 “1바이트 단위 데이터 덩어리”를 담는 그릇으로 봐야 혼동이 줄어듭니다.
        
    - 문자열로 다루려면 널 종료(\0)와 인코딩, 라인 엔딩까지 ‘문자 규칙’을 추가로 책임져야 합니다.
        

4. CRLF vs LF (줄바꿈)
    

- LF = \n (유닉스/리눅스/맥 표준)
    
- CRLF = \r\n (윈도우 표준)
    
- 텍스트 모드는 이 차이를 “읽기/쓰기 편의”로 흡수해주는 경우가 많고, 바이너리는 흡수하지 않습니다.
    
- 실무 포인트: 텍스트 처리 도구/에디터가 대부분 자동 대응하지만, “정확한 바이트 길이”가 중요한 작업(해시/암호/바이너리 직렬화)은 텍스트 모드로 하면 사고가 납니다.
    

5. C stdio vs C++ iostream(파일 입출력 스타일)
    

- C 스타일(FILE*, fopen/fclose, fprintf/fscanf, fread/fwrite)
    
    - 비교적 단순하고 빠르며, 포맷 기반 입출력에 익숙하면 쓰기 쉽습니다.
        
    - 대신 코드가 지저분해지기 쉽고, 타입 안정성이 낮습니다(포맷 실수에 취약).
        
- C++ 스트림(ifstream/ofstream/fstream, << >>, read/write, is_open)
    
    - 객체 기반이라 가독성과 확장성이 좋고, 모드 조합(ios::in|ios::out|ios::app|ios::binary 등)이 일관됩니다.
        
    - 성능 차이는 “파일 I/O 자체가 병목”인 경우가 대부분이라 실전에서 큰 의미가 적은 편입니다.
        
- 강의의 의도 포인트
    
    - 엔진/언리얼 환경에서 C 스타일 포맷 입출력과 닮은 패턴을 자주 만나서, 낯설지 않게 만들려는 목적이 큽니다.
        

6. 엔진 설정을 코드가 아니라 “설정 파일”로 뺀 이유(핵심 동기)
    

- ==바이너리(실행 파일) 업데이트== 없이 값만 바꾸고 싶다
    
    - 프레임레이트, 해상도, 각종 토글을 소스코드 재빌드 없이 바꾸는 구조
        
- 운영/서비스 관점에서 더 중요해지는 이유
    
    - 앱/게임 배포 이후, 작은 밸런스나 옵션 변경을 “데이터 교체”로 처리하면 업데이트 부담이 줄어듭니다.
        
- 구현 흐름(가장 단순한 버전)
    
    - Config/Settings.txt 같은 파일을 열고
        
    - 정해둔 포맷대로 한 줄 읽어서(frame_rate=120 같은)
        
    - 파싱해서 EngineSettings 같은 구조체에 넣고
        
    - 그 값을 기반으로 1/프레임레이트로 tick 간격 등을 계산
    