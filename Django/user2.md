## user 실습 (login/logout)

1. account 앱 생성

- `$ python manage.py startapp account`

2. 프로젝트 폴더(lionproject) - settings.py에 account앱 등록

   ```py
   # Application definition

   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'blog',
       'account',
   ]
   ```

3. account앱에 urls.py 생성

   ```py
   from django.urls import path
   from .views import *  # blog 앱에 있는 views.py에 있는 모든 함수 가져옴

   urlpatterns = [
     path('login/', login_view, name = "login"),
     path('logout/', logout_view, name= "logout"),
   ]
   ```

4. 프로젝트 폴더(lionproject) - urls.py에 account앱 url 등록

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
       path('account/', include('account.urls')),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # media를 위한 url 설정
   ```

5. login/logout 처리할 함수 account/views.py에 생성

   ```py
   from django.shortcuts import render, redirect
   from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
   from django.contrib.auth import authenticate,login,logout

   # Create your views here.
   def login_view(request):
     if request.method == 'POST':
       form = AuthenticationForm(request=request, data=request.POST)
       if form.is_valid():
         username = form.cleaned_data.get("username")
         password = form.cleaned_data.get("password")
         user = authenticate(request= request, username= username, password= password)
         if user is not None:
           login(request, user)
         return redirect("home")
     else:
       form = AuthenticationForm()
       return render(request, 'login.html', {'form':form})

   def logout_view(request):
     logout(request)
     return redirect("home")
   ```

6. account/templates 디렉토리에 login html 생성

   ```html
   {% extends 'base.html' %} {% block content %}
   <h1>Login</h1>

   <form action="{% url 'login' %}" method="post">
     {%csrf_token%} {{form.as_p}}
     <button type="submit">submit</button>
   </form>
   {% endblock %}
   ```

7. base.html navbar에 login/logout 버튼 생성 => \<a>태그 사용

   ```html
   ...

   <li class="nav-item">
     <a class="nav-link active" aria-current="page" href="{% url 'new'%}"
       >Write</a
     >
   </li>
   <li class="nav-item">
     <a class="nav-link" href="{% url 'login' %}">Login</a>
   </li>
   <li class="nav-item">
     <a class="nav-link" href="{% url 'logout' %}">Logout</a>
   </li>

   ...
   ```

8. 로그인한 user정보 표시하기 위해 home.html 수정

- lionproject/blog/templates/home.html

  ```html
  {% extends 'base.html'%} {% block content %} {% if user.is_authenticated %}
  {{user.username}} {% endif %}
  <!--유저가 authenticated되면 username 출력-->
  <h1>Blog Project</h1>
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
