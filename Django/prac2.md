## WordCount App 제작

### 복습 - 앱 제작 순서

1. App생성
2. Template 제작
3. View제작
4. URL연결

### 설계

- 문장 입력받을 template 생성 & 제출
- View에서 데이터 처리 후 결과값을 render()함수로 template로 넘겨서 사용자에게 보여줌
- input tag대신 textarea tag사용
- View 함수 -> 문자열의 단어수를 세는 코드

### 여러 개의 App을 제작할 때 URL 연결 시 문제점

- 'firstapp'과 'wordCount'모두 views.py를 가지고 있기 때문에 path()에서 어떤 views를 사용해야 할지 모호해짐

  ```py
  from django.contrib import admin
  from django.urls import path
  from firstapp import views
  from wordCount import views

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('', views.welcome, name="welcome"),
      path('hello/', views.hello, name="hello"), # 누구의 views인가?
      path('home/', views.home),                 # 누구의 views인가?
  ]
  ```

1. 해결방법1 : from 사용하지 않고 import만 사용하기

   ```py
   from django.contrib import admin
   from django.urls import path
   import firstapp.views # import만 사용
   from wordCount import views

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', firstapp.views.welcome, name="welcome"), # app이름까지 전부 명시
       path('hello/', views.hello, name="hello"),
       path('home/', views.home),
   ]
   ```

   - path가 많아질수록 번거롭고 지저분해짐
   - 추천X

2. 해결방법2 : as 사용

   ```py
   from django.contrib import admin
   from django.urls import path
   from firstapp import views as first # as사용하여 별명 붙임
   from wordCount import views as wc # as사용하여 별명 붙임

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', first.welcome, name="welcome"),
       path('hello/', first.hello, name="hello"),
       path('home/', wc.home, name="wc"),
   ]
   ```

   - 훨씬 코드가 간단해지고 알아보기 편함

### View

```py
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


def result(request):
    sentence = request.GET['sentence']  # home.html의 textarea값 가져오기

    wordList = sentence.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    return render(request, "result.html", {'fulltext': sentence, 'count': len(wordList), 'wordDict': wordDict.items})
```

- result()

  - render(request, "url", {결과값}) : 결과값을 'result.html'로 넘겨줌

    - 결과값

      1. Textarea에 입력했던 입력값 전체  
         : `'fulltext':sentence`

      2. 총 단어수  
         : `'count': len(wordList)`

      3. 딕셔너리 파일  
         : `'wordDict': wordDict.items`
         - 'wordDict': wordDict -> error 발생
         - 각 단어이름과 각 단어의 개수, 두 종류의 값을 리턴해야 함
         - 두 종류의 값을 한 개의 쌍으로 만들어서 넘기는 `.items`사용!

### 템플릿 언어

- html에서 파이썬 변수와 문법을 사용하게 해주는 언어

- 예시

```html
{%for word in wordDict %} ... {% endfor %}
<br />
{%if a == b : return a %} ... {% endif %}
<br />
{{변수명}}
```

- result.html

```html
<div style="text-align: center">
  <h2>입력한 텍스트 전문</h2>
  <div>{{fulltext}}</div>

  <h3>당신이 입력한 텍스트는 {{count}}개의 단어로 구성되어 있습니다</h3>

  <div>
    {% for word, totalCount in wordDict %} {{word}} : {{totalCount}}
    <br />
    {% endfor %}
  </div>
</div>
```

- template언어를 사용하여 wordDict의 key와 value를 \<div>태그 안에서 모두 출력해 줌
