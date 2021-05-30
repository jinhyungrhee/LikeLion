# CRUD

## Delete

- detail.html에서 '삭제하기' 링크 생성
- delete()함수에서 `Blog.objects.get(id=id)`로 전달 받은 id값에 맞는 데이터 하나를 삭제

```py
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog

...

def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
```
