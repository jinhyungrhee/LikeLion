# Database

## ORM

- Object Relation Mapping
- sql을 배워 데이터베이스에 명령을 내리지 않아도 파이썬의 객체지향적인 방법으로 데이터베이스에 데이터를 생성,삭제,수정 등 가능
- `models.py`이용

## Python 객체지향

- **class**를 이용하여 데이터베이스 테이블 표현
- class : 정보를 저장하는 형식의 틀. 같은 형식이지만 다른 정보를 가진 객체들을 찍어냄.

```py
class Blog:
  id = 숫자
  제목 = 문자
  본문 = 문자
  생성날짜 = 날짜
  글쓴이 = 문자
```
