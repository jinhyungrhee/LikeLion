## Template 상속

- 여러 html에서 중복되는 코드 부분을 base.html에 만들어 놓고 각 html에 상속을 시키는 것
- 프로젝트 폴더(lionproject) 아래 templates폴더 생성한 뒤 그곳에 base.html 생성
  - /lionprject/lionproject/templates/base.html
- `settings.py` 안에 TEMPLATES-DIRS 설정

  - /lionproject/lionproject/settings.py

  ```py
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': ['lionproject/templates'],
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

- `base.html` - 공통으로 적용되는 코드
  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>BLOG</title>
      <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x"
        crossorigin="anonymous"
      />
      <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
        crossorigin="anonymous"
      ></script>
      <style>
        body {
          text-align: center;
        }
      </style>
    </head>
    <body>
      // duplicated code
      <div class="container">{% block content %} {% endblock %}</div>
    </body>
  </html>
  ```
- `home.html` - 각 html 적용 예
  ```html
  {% extends 'base.html'%} {% block content %}
  <h1>Blog Project</h1>
  <div>
    <a href="{%url 'new'%}">write blog</a>
  </div>
  <div class="container">
    {% for blog in blogs %}
    <div>
      <h3>{{blog.title}}</h3>
      {{blog.writer}} {{blog.summary}}
      <a href="{%url 'detail' blog.id %}">...more</a>
      <br />
    </div>
    {%endfor %}
  </div>
  {% endblock %}
  ```

## urls.py를 app별로 관리하는 법

1. 프로젝트 폴더 안의 urls.py의 코드 길이는 간결해짐
2. 앱 별로 urls.py를 관리할 수 있음  
   => 협업이나 큰 프로젝트를 할 때 편리하게 사용 가능

- 각 앱 안에 `urls.py` 파일 생성

  - lionproject/blog/urls.py

  ```py
  from django.contrib import admin
  from django.urls import path
  from .views import *  # blog 앱에 있는 views.py에 있는 모든 함수 가져옴

  urlpatterns = [
    # path('admin/', admin.site.urls), # home과 admin은 필요없음!
    #path('', home, name='home'),
    path('<str:id>', detail, name='detail'),
    path('new/', new, name='new'),
    path('create/', create, name='create'),
    path('edit/<str:id>', edit, name='edit'),
    path('update/<str:id>', update, name='update'),
    path('delete/<str:id>', delete, name='delete'),
  ]
  ```

- 간단해진 프로젝트 폴더 안의 `urls.py`

  - lionproject/lionproject/urls.py

  ```py
  from django.contrib import admin
  from django.urls import path, include
  from blog.views import home
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', include('blog.urls')),
  ]
  ```
