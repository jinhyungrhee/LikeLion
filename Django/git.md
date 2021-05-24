# Git

- 개발을 진행하는 과정마다 분기점을 만들어서 필요한 경우 그 지점으로 돌아올 수 있도록 만듦
- 게임의 Save Point 같은 것

## Git vs GitHub

- Git : 혼자 작업한 내용 저장
- GitHub : git정보를 다른 사람과 공유하는 플랫폼. 프로젝트 진행 및 다른 사람과의 협업 가능.

## GitHub 시작하기

1. 계정생성

2. 새로운 레포지토리 생성

3. vscode 프로젝트 폴더 생성

4. 터미널에 명령어 입력

   - `git config --global user.name "깃허브 유저네임"`
   - `git config --global user.email "깃허브 가입이메일"`  
     -> 깃허브 이용 시 해당 정보로 작성한 것들 표시해 줌!

   - 레포지토리 quick setup 명령어 복붙 -> 계정 연결하면 로그인 없이 사용 가능!

   ```
    echo "# gitTest" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/jinhyungrhee/gitTest.git
    git push -u origin main
   ```

   -> 프로젝트 폴더와 깃허브와 연결 완료!

## git을 관리하는 명령어

- `echo "# gitTest" >> README.md` : `README.md`파일을 만들고 그 안에 "내용" 입력

  - readme : 프로그램 사용법이나 프로그램 사용에 있어 필요한 패키지 및 설치법 등을 적어줌

- `git init` : 현재 디렉토리를 새로운 깃 저장소로 초기화

  - 숨김파일로 git관련 파일들이 생성됨
  - `ls -al`로 숨김파일 확인 가능
  - 서로 다른 두 개의 프로젝트가 있으면 각각 관리되어야 하므로 `git init`을 각각의 디렉토리에서 해줘야 함!
    - 그래야 각각의 git관련 파일들이 생기고 각각의 프로젝트를 담당할 수 있음

- `git add README.md` : 본격적으로 파일을 저장하고 기록함

  - **파일의 저장 순서**
    1. 저장할 파일 선택
       - staging area에 저장할 파일들 선택해서 넣어줌 => `git add`
       - 디렉토리의 원하는 파일 개별 선택 : `git add [파일명1] [파일명2]`
       - 디렉토리 내의 모든 파일 선택 : `git add .`
       - 현재 git의 상태 확인 : `git status`
       - Untracked files : staging area에 올라가 있지 않은 파일들
       - `.gitignore` : 올라가지 말아야 할 파일의 이름들을 모아둔 파일 - filter역할(gitignore.io 참고)
    2. 선택한 파일 저장
       - staging area를 통째로 저장 => `git commit`

- `git commit -m "first commit"` : staging area의 파일들을 저장함

  - `-m "내용"` 옵션 : 커밋에 주석처럼 메시지를 남기는 것
  - `git log` 명령어 : 이전에 커밋한 내용들을 확인할 수 있음

- `git branch [브랜치 이름]` : 현재 작업중인 프로젝트에서 새로운 **분기점(branch)** 만드는 것

  - 작업을 하다가 실험적으로 새로운 작업을 하고 싶을 때
  - 여러 사람과 작업 시 코드가 겹치지 않게 따로 떨어져서 작업하고 싶을 때
  - `git init`을 하면 기본적으로 **master branch**가 자동적으로 생김
  - `-M main` 옵션 : master branch의 이름을 main으로 바꾼다는 의미
    - master branch 이름을 그대로 사용하고 싶다면 이 명령어 생략 가능
  - `git checkout [브랜치 이름]` : **생성한 브랜치로 작업파일들을 옮기는 명령어**
    ```
    $ git branch leaf
    $ git status
    >> On branch master
    >> Your branch is up to date with 'origin/master'.
    >> Untracked files: .gitignore
    $ git checkout leaf
    $ git status
    >> On branch leaf
    >> Untracted files: .gitignore
    ```

- `git remote add [remote 이름] [레포지토리 주소]` : [레포지토리 주소]를 [remote 이름]으로 연결

  - "git remote add origin https://github.com/~" : '레포지토리 주소'를 **origin**이라는 **이름**으로 연결
  - 다음부터는 **origin**이라는 **이름**으로 해당 레포지토리에 코드를 upload/download가 가능함
  - 하나의 디렉토리에 두 개의 레포지토리 연결 가능

  ```
  $ git remote add origin https://github.com/jinhyungrhee/gitTest.git
  // origin이라는 이름으로 새로운 레포지토리(gitTest)에 연결
  $ git remote add second https://github.com/jinhyungrhee/gitTest2.git
  // second라는 이름으로 새로운 레포지토리(gitTest2)에 연결
  $ git push second master
  // second라는 이름의 레포지토리에 master라는 이름의 branch에 있는 파일들 올림 - gitTest2 레포지토리에만 반영됨
  $ git push origin master
  // origin이라는 이름의 레포지토리에 master라는 이름의 branch에 있는 파일들 올림 - gitTest1 레포지토리에만 반영됨
  ```

- `git push [remote 이름] [branch 이름]` : [remote 이름] 레포지토리에 [branch 이름] branch에 있는 파일들 올림
