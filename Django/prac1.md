## App

- Django 프로젝트를 이루는 작은 단위
- 각각의 서비스 별로 분류해놓은 것
- 하나의 큰 프로젝트를 작게 쪼개서 개발, 유지보수를 용이하게 함

1. 앱 생성

- `manage.py`를 이용해서 만듦  
  ` python manage.py startapp [app이름]`

2. 프로젝트에 앱 등록하기

- 프로젝트 설정 폴더(프로젝트명과 동일)/settings.py

  ```py
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
  ]
  ```

  -> 맨 밑에 `'[앱이름].apps.[(첫글자대문자)앱이름Config]',` 추가

  - 이는 `apps.py`파일 안에 있는 class를 가져오는 것
  - 주의 : 마지막 **콤마** 빼먹지 말 것!

3.  MTV 구현

    1. Template

       - 앱 하위폴더에 html파일을 관리하는 **templates**폴더 생성
       - html파일 생성

       1. 이름 입력받는 page (welcome.html)

       ```html
       <div style="text-align: center">
         <h1>사용자의 이름을 입력해주세요</h1>
         <br />
         <form action="hello">
           <label for="nameInput"> 이름 :</label>
           <input id="nameInput" name="name" />
           <input type="submit" value="제출" />
         </form>
       </div>
       ```

       - `<form action="hello">`  
         : urls.py의 path에 있는 **url name** 입력

       2. 입력 값을 처리해서 보여주는 page (hello.html)

       ```html
       <div style="text-align: center">
         <h1>반갑습니다! {{userName}}님</h1>
       </div>
       ```

       - `template언어:{{}}`  
         : html에서 python처럼 변수나 제어문과 같은 문법을 사용할 수 있게 해주는 것

    2. View

       - `views.py` 사용

       1. 함수호출로 페이지 띄우는 방법 설정

       ```py
        from django.shortcuts import render

        def welcome(request):
            return render(request, "welcome.html")

        def hello(request):
            userName = request.GET['name']
            return render(request, 'hello.html', {'userName': userName})
       ```

       - welcome()

         - `render(request, "welcome.html")`  
           : 다른 곳에서 `welcome()`함수를 호출하면 `render()`함수를 이용해서 `welcome.html`을 띄워줌

       - hello()

         - `userName = request.GET['name']`  
           : 'welcome.html'에 있는 \<input>박스에 있는 "name" 값을 가져오는 것
         - `render(request, 'hello.html', {'userName': userName})`
           - 세번째 인자 - **딕셔너리 자료형**으로 넘겨줄 데이터 입력하면 해당 html파일로 데이터 넘어감!

       2. URL로 사이트 호출하는 방법 설정 (URL과 view함수 연결)

       - 프로젝트 설정폴더(프로젝트명)/urls.py

       ```py
        from django.contrib import admin
        from django.urls import path
        from firstapp import views # urls.py 안에서 views.py 사용하기 위해 import

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.welcome, name="welcome"), # 새로운 path 추가
            path('hello/', views.hello, name="hello"), # 새로운 path 추가
        ]
       ```

       - `path('url주소', 연결할 view함수 이름, name="")`

         - url주소

           - `''`(공백) : 서버를 기동시키고 처음 돌아가는 페이지는 view에 연결된 페이지(welcome)자체가 됨
           - **url주소는 모두 달라야 함!** -> 겹치면 어떤 view를 특정해야 할지 모르게 됨

         - name : 다른 html파일에서 전체 url를 입력하지 않고 간편하게 불러올 수 있도록 만든 url name

    3. Model

       - 이번실습에서는 데이터베이스 필요X

## 웹사이트 구동 순서

1. 사용자가 서버에 요청

2. 서버의 view는 model에게 요청에 필요한 데이터를 받음

3. view는 받은 데이터를 적절하게 처리(가공처리)해서 template으로 넘김

4. template은 받은 정보를 사용자에게 보여줌

## 실습 정리

1. App 생성

2. Template 제작

3. View 제작

4. URL 연결
