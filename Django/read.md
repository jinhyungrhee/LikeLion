# CRUD

- Create : 생성히디
- Read : 읽다
- Update : 수정하다
- Delete : 삭제하다  
  => 데이터베이스 정보를 CRUD!

## Read

- 데이터를 웹페이지 상에서 볼 수 있도록 하는 것
- html에 Blog 객체를 찍어내기

- get_object_or_404

  ```py
  from django.shortcuts import render, get_object_or_404

  def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

  ```

  - 객체가 존재하면 가져오고 없으면 404 에러 리턴
  - HTTP상태코드 404 : Not Found Error, 서버가 요청한 페이지(resource)를 찾을 수 없다.

- path converter

  ```
  urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('<str:id>', detail, name='detail'),
  ]
  ```

  - `<자료형:매개변수이름>`형태
    - 입력받는 매개변수(id값)에 따라 페이지가 다르게 보임
