# Django Framework

## Framework란?

- 프레임워크 == 라이브러리?

  - 프레임워크는 라이브러리들의 라이브러리임
  - 라이브러리에 비해 조금 더 구조가 잡혀 있어서 라이브러리에 비해 작업량이 훨씬 적음
  - 프레임워크를 쓰면 개발 속도가 빠르다
  - 개발 현장에선 한 프로젝트에 여러 라이브러리와 프레임워크를 동시에 사용한다

## vscode에서 terminal을 사용하는 이유

- vscode는 코드를 작성하는데 도움을 주는 기능을 하는 editor
- 개발은 필요한 프레임워크나 라이브러리를 다운받고 필요하면 컴파일까지 해줘야 함
- editor에는 이러한 기능이 없으므로 terminal을 사용해서 editor에 없는 기능을 사용하는 것
- terminal을 새로 띄우면 현재 열어 놓은 폴더로 위치가 변경됨

## 가상환경

- 프로젝트를 여러 개 진행하는 상황에 대비하여 설정
- 서로 다른 프로젝트에서 각각 다른 종류와 버전 사용할 가능성 多
- 매번 설정하기 번거롭고 오류 발생할 가능성이 있음
- 각각의 가상환경을 만들어 해당하는 버전을 각각 설정해 놓음
- 명령어

1. 독립된 가상환경 생성 명령어  
   `python -m venv [가상환경이름]`
2. 가상환경을 실행시키는 명령어  
   `source 가상환경이름/Scripts/activate`
3. django 다운받는 명령어  
   `pip install django`

   - pip(Python Install Package): Python Package를 다운받게 해주는 시스템

4. django로 프로젝트 만드는 명령어  
   `django-admin startproject [프로젝트이름]`

   - 새로운 프로젝트 파일 생성됨
   - `manage.py` : 프로젝트가 실행되기 위해 꼭 필요한 파일. server를 가동시키는 기능.

5. server 가동시키는 명령어(해당 프로젝트 파일로 cd후)  
   `python manage.py runserver`
