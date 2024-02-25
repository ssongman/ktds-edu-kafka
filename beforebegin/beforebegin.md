# < 시작전에 >





# 1. 실습 환경 준비(개인PC)

우리는 Kubernetes 기반에 Kafka / Redis 설치하는 실습을 진행할 것이다.

Cloud 환경에 Kubernetes가 설치된 VM 이 개인별 하나씩 준비되어 있어 있다.

그러므로 개인 PC에서 VM 접속할 수 있는 Terminal 을 설치해야 한다.



## 1.1 MobaxTerm 설치

Cloud VM에 접근하기 위해서는 터미널이 필요하다.

CMD / PowerShell / putty 와 같은 기본 터미널을 이용해도 되지만 좀더 많은 기능이 제공되는 MobaxTerm(free 버젼) 을 다운로드 하자.



- 다운로드 위치
  - 링크: https://download.mobatek.net/2362023122033030/MobaXterm_Installer_v23.6.zip

- mobaxterm 실행

![image-20220702160114315](beforebegin.assets/image-20220702160114315.png)







## 1.2 gitBash 설치

교육문서를 다운로드 받으려면 Git Command 가 필요하다. Windows 에서는 기본 제공되지 않아 별도 설치 해야 한다.

- 참조 링크 : https://git-scm.com/
- 다운로드 위치 
  - 링크 : https://github.com/git-for-windows/git/releases/download/v2.44.0.windows.1/Git-2.44.0-64-bit.exe






## 1.3 Typora 설치

교육자료는 MarkDown 문서로 되어 있으며 MD 파일을 확인하기 위해서  typora를 설치 한다.



### (1) 설치

- 참조 링크: https://typora.io/
- 다운로드 위치
  - 링크 : https://download.typora.io/windows/typora-setup-x64.exe


- Typora 실행



### (2) typora 환경설정

원할한 실습을 위해 코드펜스 옵션을 아래와 같이 변경하자.

- 코드펜스 설정
  - 메뉴 : 파일 > 환경설정 > 마크다운 > 코드펜스
    - 코드펜스에서 줄번호 보이기 - check
    - 긴문장 자동 줄바꿈 : uncheck




![image-20220702154444773](beforebegin.assets/image-20220702154444773.png)



- 개요보기 설정
  - 메뉴 : 보기 > 개요
    - 개요 : check





## 1.4 STS 설치


### (1) java 17 설치

java 17이 설치되어 있지 않은 경우에만 수행한다.

* 참고링크
  * oracle.com 링크 : https://www.oracle.com/java/technologies/downloads/#jdk17-windows
  * 설치관련 문서 : https://jiurinie.tistory.com/131

- jdk 다운로드 주소
  - 링크: https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.msi
- 설치완료후 확인

```sh
# CMD 명령 프롬프트 windows에서 ...

C:\Users\ssong>java -version
openjdk version "17.0.5" 2022-10-18
OpenJDK Runtime Environment Temurin-17.0.5+8 (build 17.0.5+8)
OpenJDK 64-Bit Server VM Temurin-17.0.5+8 (build 17.0.5+8, mixed mode, sharing)

```





### (2) STS 설치

- 참고 링크

  - STS 참조 링크: https://spring.io/tools
  - 설치관련 문서 : https://kjchoi.co.kr/17

- 다운로드 주소

  - 링크: https://cdn.spring.io/spring-tools/release/STS4/4.21.1.RELEASE/dist/e4.30/spring-tool-suite-4-4.21.1.RELEASE-e4.30.0-win32.win32.x86_64.self-extracting.jar

- 설치
  - 적당한 위치에 압축 해제 하자.

    - [참고]

      - 다운로드된 파일은 jar 파일이므로 일반적으로 더블클릭만 하면 실행파일로 압축해제 됨

      - 아래와 같은 명령으로 압축해지 해도 된다.

        - ```sh
          # 압축해제 전
          $ dir      .
          2024-02-24  오후 01:00       648,346,802 spring-tool-suite-4-4.21.1.RELEASE-e4.30.0-win32.win32.x86_64.self-extracting.jar
          
          # 압축해제
          $ java -jar spring-tool-suite-4-4.21.1.RELEASE-e4.30.0-win32.win32.x86_64.self-extracting.jar
          
          # 압축해제 후
          $ dir      .
          2024-02-24  오후 01:00       648,346,802 spring-tool-suite-4-4.21.1.RELEASE-e4.30.0-win32.win32.x86_64.self-extracting.jar
          2024-02-24  오후 01:02    <DIR>          sts-4.21.1.RELEASE
          ```

- STS 설정

  - Workspace 설정
    - STS 시작시 위치 변경
    - 위치 : C:\workspace\sts-4.21.1 

  - JRE 설정
    - STS 메뉴 :  [Window] - [Prefernces] - [Java] - [Installed JREs]
    - STS 내장된 JRE 에서 jdk-17.x  로 변경 후 apply
    - 없으면 Add 버튼으로 추가
  - Compiler 설정
    - STS 메뉴 :  [Window] - [Prefernces] - [Java] - [Compiler]
    - Compiler complicance level : 17 로 변경
  - 인코딩 변경
    - STS 메뉴 :  [Window] - [Prefernces] - [General] - [Workspace] - [Text file encoding]
    - UTF-8로 변경






# 2. 교육문서 Download

해당 교육문서는 모두 markdown 형식으로 작성되었다.  Chrome Browser 에서 github 문서를 직접 확인해도 된다.

하지만 실습을 따라가다 보면 개인별로 수정해야 할 부분이 있는데 web browser 에서는 수정이 안되기 때문에 수정이 용이한 환경이 훨씬 좋을 것이다.

좀더 효율적인 실습을 위해서 해당 자료를 download 하여 markdown 전용 viewer 인 Typora 로 오픈하여 실습에 참여하자.





## 2.1 교육문서 Download

gitbash 실행후 command 명령어로 아래와 같이 임의의 디렉토리를 생성후 git clone 으로 download 하자.

```sh
# GitBash 실행

# 본인 PC에서 아래 디렉토리를 생성
$ mkdir -p /c/githubrepo
 
 
$ cd /c/githubrepo

$ git clone https://github.com/ssongman/ktds-edu-kafka.git
Cloning into 'ktds-edu-kafka'...
remote: Enumerating objects: 181, done.
remote: Counting objects: 100% (181/181), done.
remote: Compressing objects: 100% (119/119), done.
remote: Total 181 (delta 33), reused 175 (delta 30), pack-reused 0
Receiving objects: 100% (181/181), 7.84 MiB | 6.34 MiB/s, done.
Resolving deltas: 100% (33/33), done.



$ ll /c/githubrepo
drwxr-xr-x 1 ssong 197609 0 Feb 24 12:02 ktds-edu-kafka/

```



## 2.2 Typora 로 readme.md 파일오픈



- typora 로 오픈

```
## typora 에서 아래 파일 오픈

C:\githubrepo\ktds-edu-kafka\README.md
```

![image-20220702160433029](beforebegin.assets/image-20220702160433029.png)





# 3. 실습 환경 준비(Cloud)



## 3.1 개인 VM 서버 주소 확인- ★

개인별 VM Server 접속 환경 및 Kafka 실습을 위한 개인 Topic 정보를 확인하자.

| 담당자 |        소속        | VM  Server | VM  Server IP | kafka  Topic |  kafka  Group  | 비고 |
| :----: | :----------------: | :--------: | :-----------: | :----------: | :------------: | :--: |
| 송양*  | ICIS Tr 아키텍처팀 | bastion01  |  34.xx.xx.xx  | edu-topic01  | edu-topic01-cg |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |
|        |                    |            |               |              |                |      |





강미혜(Genie서비스팀) <MI-HYE.KANG@KT.COM>;
강정현(미디어플랫폼팀) <JEONGHYEON.KANG@KT.COM>;
김경호(보안정책팀) <GYEONG-HO.KIM@KT.COM>;
김나경(플랫폼CoE팀) <NA_KYOUNG.KIM@KT.COM>;
김무한(미디어서비스팀) <MOOHAN.KIM@KT.COM>;
김민수(아키텍처팀) <MINSU74@KT.COM>;
김지훈(경영인프라팀) <JIHUN094.KIM@KT.COM>;
박승섭(데이터DX개발팀) <SEUNGSEOB.PARK@KT.COM>;
백연희(플랫폼CoE팀) <YH.BAEK@KT.COM>;
양동기(환경DX플랫폼팀) <DONG_GI.YANG@KT.COM>;
여준영(미디어플랫폼팀) <JUNYEONG.YEO@KT.COM>;
우예원(플랫폼CoE팀) <YW.WOO@KT.COM>;
유광선(플랫폼컨설팅팀) <KSYOO@KT.COM>;
이은석(에듀DX플랫폼팀) <ES.LEE@KT.COM>;
이화경(DX인프라팀) <HWAKYUNG.LEE@KT.COM>;
장진호(데이터DX개발팀) <JINHOSS.JANG@KT.COM>;
조민정(고객DX솔루션팀) <HS-CHO@KT.COM>;
조은하(플랫폼인프라팀) <EUNHA.CHO@KT.COM>;
최정우(SI개발팀) <JWOO.CHOI@KT.COM>









## 3.2 ssh (Mobaxterm) 실행

Mobaxterm 을 실행하여 VM 접속정보를 위한 신규 session 을 생성하자.

- 메뉴
  - Session  : 상단 좌측아이콘 클릭

  - SSH : 팝업창 상단 아이콘 클릭

![image-20230514022214007](beforebegin.assets/image-20230514022214007.png)

빨간색 영역을 주의해서 입력한 후 접속하자.



- Romote host
  - 개인별로 접근 주소가 다르므로 위 수강생별  VM  Server IP 주소를 확인하자.
  - ex)  bastion03 : 35.247.230.92

- User
  - Specify username 에 Check
  - User : ubuntu 입력

- Port : 22
- Advanced SSH settings
  - Use private key : C:\githubrepo\ktds-edu-kafka\vm-key\ktdseduuser
    - 교육자료 Download 되는 자료에 위 key가 포함되어 있음






## 3.3 VM 서버에서 실습자료 download

실습 테스트를 위해서 실습 자료를 받아 놓자.

이미 각자 VM에 해당 교육자료가  git clone 되어 있으므로 git pull 로 최신 데이터로 update 만 진행하자

```sh

# 최신 데이터를 한번 더 받는다.
$ cd ~/githubrepo/ktds-edu-kafka
$ git pull



# 만약 pull일 잘 안되는 경우는 모두 삭제후 다시 git clone 받자.

# 삭제
$ rm -rf ~/githubrepo/ktds-edu-kafka/

$ cd ~/githubrepo

## git clone 수행
$ git clone https://github.com/ssongman/ktds-edu-kafka.git
Cloning into 'ktds-edu-kafka'...
remote: Enumerating objects: 320, done.
remote: Counting objects: 100% (320/320), done.
remote: Compressing objects: 100% (220/220), done.
remote: Total 320 (delta 95), reused 277 (delta 56), pack-reused 0
Receiving objects: 100% (320/320), 8.40 MiB | 24.22 MiB/s, done.
Resolving deltas: 100% (95/95), done.


# 확인
$ cd  ~/githubrepo/ktds-edu-kafka

$ ll ~/githubrepo/ktds-edu-kafka
drwxrwxr-x 8 ktdseduuser ktdseduuser 4096 Sep  3 12:27 .git/
-rw-rw-r-- 1 ktdseduuser ktdseduuser  382 Sep  2 13:45 .gitignore
-rw-rw-r-- 1 ktdseduuser ktdseduuser 4006 Sep  2 13:45 README.md
-rw-rw-r-- 1 ktdseduuser ktdseduuser  461 Sep  2 13:45 SUMMARY.md
drwxrwxr-x 4 ktdseduuser ktdseduuser 4096 Sep  3 12:27 beforebegin/
drwxrwxr-x 4 ktdseduuser ktdseduuser 4096 Sep  2 13:45 cloud-setup/
drwxrwxr-x 2 ktdseduuser ktdseduuser 4096 Sep  2 13:51 gcp-vm-key/
drwxrwxr-x 7 ktdseduuser ktdseduuser 4096 Sep  3 12:27 kafka/
drwxrwxr-x 8 ktdseduuser ktdseduuser 4096 Sep  2 13:45 redis/


```



## [참고] git repo 초기화 방법

수정된 파일이 존재하여 git pull 이 잘 안될때는 삭제후 다시 Clone 하는 방법도 있지만

내용이 많다거나 다른 사유로 인해 clone 작업이 힘들 경우 아래와 같은 명령어를 사용해도 된다.

```sh
# 1) 마지막 commit hash 값으로 reset 처리
## 아직 staged 에 올라가지 않은 수정파일,  untracked file 까지 모두 사라진다.
$ git reset --hard HEAD~
$ git pull



# 2) untrackted file 을 초기화 해야 하는 경우
$ git clean -f -d
$ git pull


# 3) 파일단위로 restore 를 원할 경우
$ git restore modified_file
$ git pull


# 4) stash
# stash 는 내가 수행한 작업을 commit 하기전 임시로 저장해 놓는 명령이다.
$ git stash
$ git pull


# 참고
## commit log 확인
$ git
```

