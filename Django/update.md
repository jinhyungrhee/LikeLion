# CRUD

## Update

- edit() : edit.html을 보여줌
- update() : 수정내역을 데이터베이스에 적용
- Create기능 구현과 거의 동일!
  - 차이점 : **Update는 수정할 데이터의 id값을 받아야함** => path converter 사용
    - 수정해야 할 데이터를 데이터베이스에서 불러서 new.html 형식에 기존 정보들을 다시 덮어씌우는 과정 필요
    - views.py에서 매개변수를 받아서 사용하고 싶다면 urls.py에서 path converter(`<str:id>`)를 반드시 써야 하고  
      path converter를 사용하면 \<a>태그 - `<a href="{% url 'edit' blog.id %}">수정하기</a>`(detail.html)와  
      \<form>태그 - `<form action="{%url 'update' blog.id %}" method="post">`(edit.html)에서 넘겨줄 인자로 **id를 명시**해야 함!
