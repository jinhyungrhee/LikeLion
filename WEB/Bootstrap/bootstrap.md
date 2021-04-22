# Bootstrap

- Twitter 개발자들이 만든 CSS/JavaScript기반 웹 프레임워크
- 장점 :
  - 오픈소스
  - 반응형 웹 지원(자동화면조정)
  - 브라우저 호환성
- 단점 :
  - 갖다 쓴 티가 남
  - 성능이 다소 떨어짐

## Bootstrap 시작하기

1. Bootstrap CDN링크들을 html 파일 \<head>태그에 붙여 넣음

- CDN링크를 주소창에 넣어보면 온갖 css코드들이 등장함  
  ➡ '온갖 디자인 요소들을 아래에 있는 코드에 끌어다 쓰겠다'는 의미!
- '개발자도구(F12)-Network'에 들어가서 새로고침(F5)  
  ➡ bootstrap 요소가 확인되었음을 볼 수 있음
- console : 'Uncaught Error: Bootstrap's JavaScript requires jQuery' 에러 메시지  
  ➡ jQuery가 없어서 아직 사용할 수 없음

2. jQuery CDN링크를 html 파일 \<head>태그 맨 윗 부분에 붙여 넣음

- 'http://code.jquery.com/'

## Container

- html과 달리 양 쪽에 여백을 만들어 주는 것

```html
<div class="container"></div>
```
