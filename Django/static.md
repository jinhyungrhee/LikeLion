## 장고에서 다루는 파일

1. 정적 파일

- 미리 서버에 저장되어 있는 파일
- 서버에 저장된 그대로를 서비스해주는 파일

  1. static 파일

     - 개발자가 서버를 개발할 때 미리 넣어 놓은 정적파일(img, js, css)

  2. media 파일

     - 사용자가 업로드 할 수 있는 파일

2. 동적 파일

- 서버의 데이터들이 어느 정도 가공된 다음 보여지는 파일
- request, POST/GET 등 상황에 따라 달라질 수 있음

## Static 파일

```py
import os

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'blog', 'static')]  # 현재 static 파일들이 어디에 있는지 경로 표시

STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # static 파일을 어디에 모을건지
```

- static 파일 모으기
  - `$ python manage.py collectstatic`
  - 프로젝트 폴더(likelion) 하위에 static 폴더 생성

```
$ python manage.py collectstatic

Found another file with the destination path 'likelion.png'. It will be ignored since only the first encountered file is collected. If this is not what you want, make sure every static file has a unique path.

129 static files copied to 'C:\Users\Jinhyung\Desktop\django\lionproject\static'.
```

    => 실서버 배포시 정적 파일들을 편리하기 관리하기 위해서 모으는 것!

## Static 파일을 모든 페이지에 띄우는 방법

- `base.html`의 body부분에 `{% load static %}`입력
- 이미지 태그 사용 : `<img src = "{% static 'likelion.png'%}" alt = "">`

```html
<body>
  {% load static %}
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <!-- navbar로고 부분에 <img />태그로 이미지 넣어줌 -->
      <!--href에 template 상속하여 이미지 누르면 홈화면으로 이동하도록 만듦 -->
      <a class="navbar-brand" href="{%url 'home'%}">
        <img src="{% static 'likelion.png'%}" alt="" width="50" height="35" />
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      ></button>
      ...
    </div>
  </nav>
</body>
```
