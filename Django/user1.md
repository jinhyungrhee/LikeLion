## user 모델

- 장고가 제공하는 user 모델

  - `myvenv/Lib/site-packages/django/contrib/auth/models.py`

- 기존 user 모델로는 정보가 부족해 컬럼을 더 추가해야하는 경우

  - user를 대체할 테이블을 만들어야 함!
  - 장고에서 제공하는 user클래스를 우리가 만들 user로 바꿔치기함

- 장고에서 제공해주는 auth 모듈
  1. authenticate
     - client에서 login 요청을 했을 때 그 요청 정보의 username과 password가 user table의 user의 정보와 일치하는지 확인해주는 함수
  2. login
     - user table에서 온 user 객체를 통해 client가 인증될 수 있게 해주는, 인증된 상태를 만들어주는 함수
     - login이 되어 인증된 상태가 되면 user객체가 request정보에 포함되어 server로 날아가게 됨
  3. logout
     - 인증된 user가 server에게 인증을 풀어달라고 요청을 하는 함수
