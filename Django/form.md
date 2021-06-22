## form

- django에서 어떠한 입력받는 공간을 주는 것
- forms.py를 통해 form을 만들면 데이터베이스의 모델이 변할때마다 일일이 바꿔주지 않아도 됨
- method를 통해서 유효성 검사를 더 편리하게 할 수 있음

- `forms.py`생성

  ```py
  from django import forms
  from .models import Blog

  class BlogForm(forms.ModelForm):
    class Meta:
      model = Blog
      fields = ['title', 'writer', 'body', 'image']
  ```

  => class안의 class인 Meta class 사용  
  => `models.py`에서 pub_date를 제외한 나머지 것들 fields로 포함시킴

- `new.html`에 적용

  ```html
  {% extends 'base.html' %} {% block content %}
  <h1>Write Your Blog</h1>

  <form action="{%url 'create'%}" method="post" enctype="multipart/form-data">
    {%csrf_token%} {{form.as_p}}
    <button type="submit">submit</button>
  </form>
  {% endblock %}
  ```

  => `{{form.as_p}}` : form을 \<p>태그로 받음

- `views.py`-create에도 적용 가능

  ```py
  from django.shortcuts import render, redirect, get_object_or_404
  from django.utils import timezone
  from .models import Blog
  from .forms import BlogForm # BlogForm import!

  ...

  def create(request):
      form = BlogForm(request.POST, request.FILES)
      if form.is_valid(): # 유효성 검사
          new_blog = form.save(commit=False) # 임시저장
          new_blog.pub_date = timezone.now()
          new_blog.save()
          return redirect('detail', new_blog.id)  # 요청이 보내졌을 때 어떤 화면으로 이동할 것인지 리턴
      return redirect('home')

  ```

  => if문 사용해 유효성 검사 필요!
