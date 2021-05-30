# CRUD

## Create

- new() : new.html을 보여줌
- create() : new.html에서 받은 정보를 데이터베이스에 저장

## GET vs POST

| GET                     | POST                        |
| ----------------------- | --------------------------- |
| 데이터를 얻기 위한 요청 | 데이터를 생성하기 위한 요청 |
| 데이터가 url에 보임     | 데이터가 url에서 안보임     |
|                         | Csrf 공격 방지              |

- 보안을 위해 데이터베이스에 접근할 때에는 반드시 **POST방식** 사용!
- CSRF(Cross-Site Request Forgery) : 사이트 간 요청 위조. 서버가 공격자에 의해 데이터베이스에 수정,삭제 요청을 하는 것

  - 이를 방지하기 위해 \<form>안에 `{%csrf_token%}` 템플릿 변수 명시

    ```html
    <form action="" method="post">
      {%csrf_token&}
      <p>제목:<input type="text" name="title" /></p>
      <p>작성자:<input type="text" name="writer" /></p>
      본문: <textarea name="" id="" cols="30" rows="10"></textarea>
      <button type="submit">submit</button>
    </form>
    ```

## redirect

- 요청이 보내졌을 때 어떤 화면으로 이동할 것인지 리턴

```py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

...

def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id) # 새로 생성한 detail로 이동(id값 이용해서)
```
