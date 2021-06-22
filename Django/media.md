## media

- 사용자가 업로드 할 수 있는 파일

- `urls.py`수정

  ```py
  from django.contrib import admin
  from django.urls import path, include
  from blog.views import home
  from django.conf import settings
  from django.conf.urls.static import static

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', home, name='home'),
      path('blog/', include('blog.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media를 위한 url 설정
  ```

- `upload_to`

  - 업로드할 폴더를 지정하는 것
  - `settings.py`에 MEDIA_URL로 지정해둔 media 폴더 안에 blog폴더를 만들어서 관리하겠다는 설정
  - `lionproject/blog/models.py`

  ```py
  from django.db import models

  # Create your models here.

  class Blog(models.Model):
      title = models.CharField(max_length=200)
      writer = models.CharField(max_length=100)
      pub_date = models.DateTimeField()
      body = models.TextField()
      image = models.ImageField(upload_to = "blog/", blank=True, null=True)

      def __str__(self):  # override
          return self.title

      def summary(self):  # 요약해주는 메서드 - 본문 100자
          return self.body[:100]
  ```

  - `image = models.ImageField(upload_to = "blog/", blank=True, null=True)`
    - 이 데이터베이스 컬럼에 이미지를 가리키는 url 경로가 적히는 것임

- 데이터 삭제

  - 기존의 데이터에 새로운 칼럼을 추가했을 때 에러가 발생할 수 있으므로 기존 데이터들을 삭제해줌
    - `django/lionproject/blog/migrations/0001_initial.py` 삭제
    - `django/lionproject/blog/migrations/0001_initial.cpython-38.pyc`삭제
    - `django/lionproject/db.sqlite3`삭제

- 필로우(pillow) 모듈 설치

  - `$ pip install pillow`
  - 이미지 필드 사용하기 위해 필요한 모듈

- 다시 migration하여 새로운 데이터 생성

  - `$ python manage.py makemigrations`

  ```
  $ python manage.py makemigrations
  Migrations for 'blog':
    blog\migrations\0001_initial.py
      - Create model Blog
  ```

  - `$ python manage.py migrate`

  ```
  $ python manage.py migrate
  Operations to perform:
    Apply all migrations: admin, auth, blog, contenttypes, sessions
  Running migrations:
    Applying contenttypes.0001_initial... OK
    Applying auth.0001_initial... OK
    Applying admin.0001_initial... OK
    Applying admin.0002_logentry_remove_auto_add... OK
    Applying admin.0003_logentry_add_action_flag_choices... OK
    Applying contenttypes.0002_remove_content_type_name... OK
    Applying auth.0002_alter_permission_name_max_length... OK
    Applying auth.0003_alter_user_email_max_length... OK
    Applying auth.0004_alter_user_username_opts... OK
    Applying auth.0005_alter_user_last_login_null... OK
    Applying auth.0006_require_contenttypes_0002... OK
    Applying auth.0007_alter_validators_add_error_messages... OK
    Applying auth.0008_alter_user_username_max_length... OK
    Applying auth.0009_alter_user_last_name_max_length... OK
    Applying auth.0010_alter_group_name_max_length... OK
    Applying auth.0011_update_proxy_permissions... OK
    Applying auth.0012_alter_user_first_name_max_length... OK
    Applying blog.0001_initial... OK
    Applying sessions.0001_initial... OK
  ```

- superuser 생성

  - db.sqlite3 삭제하면서 superuser 정보도 삭제됨
  - `$ python manage.py createsuperuser`

- `new.html`에 사진 input 추가

  - \<input>태그 타입 = "file"
  - 인코딩타입(enctype) 추가

    ```py
    {% extends 'base.html' %} {% block content %}
    <h1>Write Your Blog</h1>

    <form action="{%url 'create'%}" method="post" enctype="multipart/form-data">
      {%csrf_token%}
      <p>제목:<input type="text" name="title" /></p>
      <p>작성자:<input type="text" name="writer" /></p>
      <p>사진: <input type="file" name="image" /></p>
      본문: <textarea name="body" id="" cols="30" rows="10"></textarea>
      <button type="submit">submit</button>
    </form>
    {% endblock %}
    ```

- `detail.html` 수정

  ```html
  {% extends 'base.html' %} {% block content %}
  <h1>{{blog.title}}</h1>
  <div>
    작성자:{{blog.writer}}
    <br />
    날짜:{{blog.pub_date}}
  </div>
  <hr />
  <!--blog에 image가 있을 경우 tag를 보여주도록 하겠다-->
  {% if blog.image %}
  <p><img src="{{blog.image.url}}" alt="" /></p>
  {% endif %}
  <p>{{blog.body}}</p>
  <a href="{% url 'edit' blog.id %}">수정하기</a>
  <a href="{% url 'delete' blog.id %}">삭제하기</a>
  {% endblock %}
  ```
