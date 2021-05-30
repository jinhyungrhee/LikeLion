# Model실습

- 기본적인 테이블 뼈대를 만들고 데이터를 입력함

## 블로그 만들기

1. `settings.py`에 app등록

   ```py
   ...
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'blog',
   ]
   ...
   ```

2. `models.py`에 클래스 생성

   ```py
   from django.db import models

   class Blog(models.Model):
       title = models.CharField(max_length=200)
       writer = models.CharField(max_length=100)
       pub_date = models.DateTimeField()
       body = models.TextField()

   ```

   - 클래스의 이름은 테이블 이름(Blog)과 같아야 함
   - import한 models모듈 안에 있는 Model이라는 클래스 상속받음
   - Id 칼럼을 굳이 생성하지 않아도 되는 이유  
     : 상속받은 Model 클래스 안에 id값이 이미 정의가 되어 있음!

   - models 모듈
     |필드타입|HTML위젯|필수옵션|설명|
     |--|--|--|--|
     |BooleanField|CheckboxInput|-|'True/False'값을 가지는 필드|
     |CharField|TextInput|max_length|문자열 데이터를 저장하는 필드. 최대 글자 수를 반드지 지정해야 함|
     |DateField|TextInput|-|datetime.date 인스턴스인 날짜 데이터를 저장하는 필드. 달력 위젯과 오늘 날짜 입력 기능 기본제공|
     |DateTimeField|TextInput|-|datetime.datetime 인스턴스인 날짜와 시간 데이터를 저장하는 필드. 두 개의 TextInput, 달력 위젯, 오늘 날짜 입력 기능 기본제공|
     |FloatField|NumberInput|-|Python의 float과 같은 실수 데이터를 저장하는 필드|
     |IntegerField|NumberInput|-|Python의 integer과 같은 정수 데이터를 저장하는 필드. -2147483648과 2147483647 사이의 값 저장 가능|
     |TextField|Textarea|-|글자 수 제한이 없는 문자열 데이터를 저장하는 필드. max_length 값을 지정하면 폼에서는 제한이 되지만, 데이터베이스에는 영향을 주지 않음|

   - 필드 옵션
     |옵션|설명|
     |--|--|
     |blank|validation시에 empty 허용하는지|
     |null|null값 허용하는지|
     |db_index|인덱스 필드인지|
     |default|디폴트 값이나 함수를 지정해줌|
     |unique|현재 테이블 내 유일한 값인지|
     |...|...|

3. 테이블 생성 명령어 입력

   - `$ python manage.py makemigrations` 입력

     - makemigrations : 앱 내의 migration 폴더를 만들어서 models.py의 변경사항 저장
     - '이런 테이블을 만들 것이다'라는 것을 migrations 폴더에 저장시키는 것
     - 성공 : `Create model Blog` 메시지 출력

   - `$ python manage.py migrate` 입력
     ```
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
     - migrate : Migration 폴더를 실행시켜 데이터베이스에 적용
     - migrations 폴더의 변경사항들을 확인한 뒤 `db.sqlite3` 데이터베이스에 적용시킴
     - 모델에 변경사항이 있을 경우 `makemigrations`먼저 한 뒤 `migrate` 입력

4. `admin.py`에 등록하기

   ```
   from django.contrib import admin
   from .models import Blog
   # Register your models here.
   admin.site.register(Blog)
   ```

   - `models.py`에서 만든 Blog 테이블을 admin 사이트에 등록하는 것

## admin 패널

- migration한 데이터베이스 테이블들을 쉽게 확인할 수 있음

  ```
  urlpatterns = [
    path('admin/', admin.site.urls),
  ]
  ```

  - admin은 django 처음 세팅시 urls.py에 path로 연결되어 있음!
  - `http://127.0.0.1:8000/admin`을 입력하면 admin 페이지로 접속됨
  - admin 페이지는 데이터베이스를 관리하기 때문에 아무나 접근하면 안됨 => 관리자 권한을 가진 **superuser**를 생성해야 함
    - `$ python manage.py createsuperuser` 명령어 사용

## 메소드 오버라이딩(Overriding)

```py
from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):  # override
        return self.title
```

- `__str__` : 어디선가 객체가 호출이 되었을 때 나타나는 이름(이름표)같은 것
- `__str__`의 default값인 'Blog object'가 자동적으로 나타남
- 메소드 오버라이딩을 통해 객체가 호출되었을 때 '글의 제목'이 나타나도록 함
