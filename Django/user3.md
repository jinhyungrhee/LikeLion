## user 실습 (sign up)

1. signup.html 생성

   ```html
   {% extends 'base.html' %} {% block content %}
   <h1>Sign Up</h1>
   <!-- register_view에서 다 처리할 수 있게 만듦-->
   <form action="{% url 'signup' %}" method="post">
     {%csrf_token%} {{form.as_p}}
     <button type="submit">submit</button>
   </form>
   {% endblock %}
   ```

2. views.py에 register_view 함수 추가

   ```py
   from django.shortcuts import render, redirect
   from django.contrib.auth.forms import AuthenticationForm
   from django.contrib.auth import authenticate,login,logout
   from .forms import RegisterForm

   ...

   def register_view(request):
     if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
         user = form.save() # form안에 적어주는 정보 외에 꼭 필요한 정보가 없기 때문에 commit넣지 않음
         login(request, user)
       return redirect('home')
     else:
       form = RegisterForm()
       return render(request, 'signup.html', {'form':form})
   ```

3. urls.py에 path 등록

   ```py
   from django.urls import path
   from .views import *  # blog 앱에 있는 views.py에 있는 모든 함수 가져옴

   urlpatterns = [
     path('login/', login_view, name = "login"),
     path('logout/', logout_view, name= "logout"),
     path('register/', register_view, name="signup"),
   ]
   ```

   => 여기까지는 django에서 제공하는 기본 user 폼 사용한 것

4. AbstractUser 상속받아 확장된 user 폼 생성 - models.py 생성

   ```py
   from django.db import models
   from django.contrib.auth.models import AbstractUser

   # Create your models here.
   class CustomUser(AbstractUser):
     nickname = models.CharField(max_length=100)
     university = models.CharField(max_length=50)
     location = models.CharField(max_length=200)
   ```

5. settings.py에 CustomUser등록 (django에서 제공하는 기본 user모델 대체)

   ```py
   ...
   ALLOWED_HOSTS = []

   AUTH_USER_MODEL = 'account.CustomUser' # 우리가 인증하는 user모델로 사용하겠다고 알려줌, django에서 제공하는 user모델 대체
   # 설정 후 migartion 필요

   ...
   ```

   => 새로운 CustomUser 모델 생성했으므로 `$ python manage.py makemigrations`와 `$ python manage.py migrate` 해줌

   ```
   $ python manage.py makemigrations
   Migrations for 'account':
     account\migrations\0001_initial.py
     - Create model CustomUser
   ```

   ```
   $ python manage.py migrate
   Traceback (most recent call last):
     File "manage.py", line 22, in <module>
       main()
     File "manage.py", line 18, in main
       execute_from_command_line(sys.argv)
     File "C:\Users\Jinhyung\Desktop\django\myvenv\lib\site-packages\django\core\management\__init__.py", line 419, in execute_from_command_line
       utility.execute()
     File "C:\Users\Jinhyung\Desktop\django\myvenv\lib\site-packages\django\core\management\__init__.py", line 413, in execute
       self.fetch_command(subcommand).run_from_argv(self.argv)
     File "C:\Users\Jinhyung\Desktop\django\myvenv\lib\site-packages\django\core\management\base.py", line 354, in run_from_argv
       self.execute(*args, **cmd_options)
     File "C:\Users\Jinhyung\Desktop\django\myvenv\lib\site-packages\django\core\management\base.py", line 398, in execute
       output = self.handle(*args, **options)
     File "C:\Users\Jinhyung\Desktop\django\myvenv\lib\site-packages\django\core\management\base.py", line 89, in wrapped
       res = handle_func(*args, **kwargs)
     File "C:\Users\Jinhyung\Desktop\django\myvenv\lib\site-packages\django\core\management\commands\migrate.py", line 95, in handle
       executor.loader.check_consistent_history(connection)
     File "C:\Users\Jinhyung\Desktop\django\myvenv\lib\site-packages\django\db\migrations\loader.py", line 306, in check_consistent_history
       raise InconsistentMigrationHistory(
   django.db.migrations.exceptions.InconsistentMigrationHistory: Migration admin.0001_initial is applied before its dependency account.0001_initial on database 'default'.
   ```

   => migrate시 error 발생  
    => 프로젝트 폴더(lionproject)의 settings.py와 urls.py에서 admin관련된 것들 임시로 주석처리

   - settings.py

   ```py
   INSTALLED_APPS = [
     #'django.contrib.admin',
     'django.contrib.auth',
     'django.contrib.contenttypes',
     'django.contrib.sessions',
     'django.contrib.messages',
     'django.contrib.staticfiles',
     'blog',
     'account',
   ]
   ```

   - urls.py

   ```py
   #from django.contrib import admin
   from django.urls import path, include
   from blog.views import home
   from django.conf import settings
   from django.conf.urls.static import static

   urlpatterns = [
       #path('admin/', admin.site.urls),
       path('', home, name='home'),
       path('blog/', include('blog.urls')),
       path('account/', include('account.urls')),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media를 위한 url 설정
   ```

   => migrate 완료 후 다시 주석 처리 해제함

   ```
   $ python manage.py migrate
   Operations to perform:
     Apply all migrations: account, auth, blog, contenttypes, sessions
   Running migrations:
     Applying account.0001_initial... OK
   (myvenv)
   ```

6. forms.py 생성

   ```py
   from django.contrib.auth.forms import UserCreationForm
   from .models import CustomUser

   class RegisterForm(UserCreationForm): # custom user에 맞는 회원가입 폼 생성
     class Meta:
       model = CustomUser
       fields = ['username', 'password1', 'password2', 'nickname', 'location', 'university']
   ```

7. base.html에 Sign up 버튼 등록

   ```html
   <!-- 유저가 로그인 되어있을 때 write와 Logout 가능하도록 if문 처리 -->
   {% if user.is_authenticated %}
   <li class="nav-item">
     <a class="nav-link active" aria-current="page" href="{% url 'new'%}"
       >Write</a
     >
   </li>
   <li class="nav-item">
     <a class="nav-link" href="{% url 'logout' %}">Logout</a>
   </li>
   {% endif %}
   <!-- 로그인 되지 않았을 때 login과 sign up 나타나도록 if문 처리 -->
   {% if not user.is_authenticated %}
   <li class="nav-item">
     <a class="nav-link" href="{% url 'login' %}">Login</a>
   </li>
   <li class="nav-item">
     <a class="nav-link" href="{% url 'signup' %}">Sign Up</a>
   </li>
   {% endif %}
   ```

8. admin.py를 작성하여 CustomUser로 등록된 user정보 저장/관리

   ```py
   from django.contrib import admin
   from .models import CustomUser

   # Register your models here.

   admin.site.register(CustomUser)
   ```
