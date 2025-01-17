# HTML 기초 문법(요소와 태그)

## \<HTML>

- 컨텐츠의 구조를 정의하는 마크업 언어

## \<HTML 요소(Element)>

- 구성

1. 시작태그 : \<h1>
2. 내용 : 안녕하세요
3. 종료태그 : \</h1>

## \<HTML 태그(tag)>

- 태그 : 내용을 나누고 어떤 역할을 하는지 구조를 정의
- 시작태그 : 컨텐츠의 시작을 표시
- 종료태그 : 컨텐츠의 끝을 표시

## \<HTML 문서 구조>

- HTML 요소 뿐만 아니라 '정해진 양식'을 갖춰야 웹 브라우저에서 HTML을 제대로 인식할 수 있음

1. \<!DOCTYPE html> : 문서 형식을 정의. html코드는 아님! HTML5 버전의 선언 방식.
2. \<html lang="kr"> : 본격적인 태그의 시작. 사용하는 주 언어를 정의.
3. \<head> : html 문서에 대한 정보를 담고 있는 부분

   - \<meta charset="uft-8"> : 문서와 관련된 정보를 담음
   - \<title> : 웹 페이지의 제목을 담음

4. \<body> : html에서 실질적으로 보여지는 부분

## \<레이아웃과 관련된 기본 태그>

- 시맨틱 태그(Semantic tag)

  = 의미를 가지고 있는 태그

1. \<header> : 제목이나 소개를 담는 태그
2. \<nav> : 페이지 이동을 위한 메뉴를 담는 태그
3. \<section> : 기준에 맞게 구간을 나누는 태그
4. \<article> : 주 내용을 담기 위한 태그
5. \<aside> : 광고나 사이트 주변 부분의 내용을 담는 태그
6. \<footer> : 웹 사이트 가장 아래 부분에 사이트 추가 정보를 담기 위한 태그

## \<텍스트와 관련된 태그>

1. 제목 태그 : 제목을 나타내고 싶을 때 사용. 중요도에 따라 1~6까지 씀
   - \<h1> ~ \<h6>
2. 본문 태그

   - \<p>태그 : **p**aragraphs(단락, 문단)

   - \<br>태그 : **b**reak(줄바꿈), 종료태그 사용X
     - 종료태그 사용하지 않는 요소 ➡ "빈 요소(Empty element)" : \<br>, \<img> 등
   - \<pre>태그 : **pre**formatted(형식화된)
     - 적은 내용 그대로 브라우저에 표시

3. 글자와 관련된 태그
   - \<strong>태그 : bold
   - \<em>태그 : italic
   - \<sub>태그 : **sub**scripted(아래에 기입한)
   - \<sup>태그 : **sup**erscripted(위에 기입한)
   - \<ins>태그 : 밑줄(inserted, 끼워 넣은)
   - \<del>태그 : 취소선(deleted, 삭제된)

## \<링크 태그>

- 하이퍼 링크(Hyper Link)

  - 하이퍼 텍스트를 가능하게 하는 가장 주요한 도구

    = 주소 링크

- URL(Uniform Resource Locator)

  - 인터넷에서 HTML 페이지, CSS 문서, 이미지 등 자원(Resource)의 위치를 나타냄

    = 주소(Address 또는 도메인) + 경로(Path)

  1. 절대 URL(Absolute URL)

     - 접근하는 최초 시작점부터 경유한 경로를 모두 기록하여 리소스의 위치를 나타냄

  2. 상대 URL(Relative URL)

     - 기준점을 기준으로 상대적인 경로를 기록하여 리소스의 위치를 나타냄

1. \<a>태그
   - anchor(닻)과 같은 역할을 하는 태그
   - `속성(attribute)`이 따라 붙음
     - 태그에 대해 *추가적인 정보*를 제공하는 것. HTML의 모든 태그는 속성을 가질 수 잇음!
     - \<a `키="값"`>구글\</a>
     1. **`href`** : **h**ypertext **ref**erence. 연결할 웹 사이트 주소를 담고 있음.
     2. **`target`** : 클릭으로 링크를 열 때 어디에 오픈할 것이지 정하는 속성
        - target="\_self" : 현재 탭에서 링크를 여는 속성
        - target="\_blank" : 새 탭(창)에서 링크를 여는 속성

## \<멀티미디어와 관련된 태그>

1. 이미지 태그

- \<img src="이미지 URL" alt="사진 설명">
  1. src 속성  
     : 불러올 이미지의 URL을 속성값으로 가짐. src는 source(근원)의 약자.
  2. alt 속성  
     : 불러올 이미지가 없거나 불러오는데 실패했을 경우에 대신 표시되는 문장. alternative text(대체 문구)의 약자.
  3. weight/height 속성
     : 이미지의 높이와 너비를 지정할 때 쓰는 속성. **CSS에서 조정하는 것이 바람직!**

2. 유튜브 영상

- 유튜브 '공유'버튼 - 링크 공유 '퍼가기' - \<iframe> 코드 복사/붙여넣기
- \<iframe>태그 : 유튜브 영상 뿐만 아니라 웹 페이지를 삽입할 때에도 사용됨

## \<테이블과 리스트>

- 테이블

  - 테이블(표)의 구성

  1.  '표 전체'를 감싸는 태그 : **`\<table>`**
  2.  표에서 '행'을 구분하는 태그 : **`\<tr>`** (table row)
  3.  표의 행 내부에 '제목 셀'을 담는 태그 : **`\<th>`** (table heading)
  4.  표의 행 내부에 '데이터 셀'을 담는 태그 : **`\<td>`** (table data)

  - 속성

  1.  rowspan="숫자"
      : "숫자"만큼 셀이 행을 점유
  2.  colspan="숫자"
      : "숫자"만큼 셀이 열을 점유

- 목록(List)

  1.  순서 없는 목록(Unordered List) :\<ul> \<li>
  2.  순서 있는 목록(Ordered List) : \<ol> \<li>

  - 속성
    : 모두 '순서 있는 목록(ol)'과 관련. **순서**에 관여함!

    - \<ol>태그

      1. start="숫자" : 리스트가 시작하는 숫자를 정함
      2. type="문자" : 순서를 시작하는 문자를 정함
      3. reversed : 순서를 반대로 시작. 다른 속성과 달리 키(key)만 써서 사용

    - \<li>태그
      - value="숫자" : 해당하는 리스트 아이템의 번호를 지정

## \<폼 태그>

- 폼에 포함되는 다양한 입력 양식 태그들을 감싸줌
- 중요한 속성

  1.  action : 데이터를 보낼 URL 지정. 해당 **데이터를 처리할 웹 서버 URL**을 담음.
  2.  method

  - **보내는 방식**을 지정. 둘 다 브라우저에서 \<form>에 입력한 데이터를 서버로 보내는 기능.
  - 서버로 데이터를 보낼 때 정해진 메시지(HTTP Request Message)에 담아서 보냄
  - HTTP Request Message는 크게 'Header'와 'Body' 두 부분으로 나뉨. 일반적으로 'Header'부분에 목적지가 되는 서버의 URL을 적음.
    - `method="get"`  
      : 브라우저에서 \<form>에 입력한 데이터를 URL 끝에 붙여 눈에 보이게 보냄. 주소와 데이터를 함께 적어서 서버로 보냄.(=엽서)  
      **데이터 조회**만을 목적으로 할 때 주로 사용.
    - `method="post"`  
      : \<form>에 입력한 데이터를 URL 끝에 붙이지 않고 보이지 않도록 'Body'부분에 숨겨서 보냄.(=편지)  
      서버에 있는 **데이터를 쓰거나 수정, 삭제**할 때 주로 사용.

- \<input>태그

  - 사용자에게 입력을 받기 위해 사용되는 태그, 빈 태그
  - 속성
    - `type="text"` : \<input>태그의 종류를 결정
    - `name="id"` : \<input>태그 중 같은 타입과 구분되는 이름을 결정. name속성을 key로, 입력받은 데이터를 값(value)으로 전송
    - `placeholder="아이디를 입력하세요"` : input에 아무 값도 입력되지 않았을 때 나타나는 텍스트 (실제 값 X)
    - `value="초기값"` : 실제 할당되는 값. 우리가 데이터를 넣으면 이 속성에 값이 들어감. 초기값처럼 둘 수 있음.

- \<label>태그

  - 해당하는 라벨을 클릭 시 \<input>태그가 활성화 됨
  - \<input>태그의 id속성과 세트로 사용됨. 주로 \<input>태그 앞에 위치함.
  - \<form>이 어떤 역할을 하는지 알려주는 이름표와 같은 역할
  - 브라우저에서 \<label>태그를 클릭하면 입력란이 활성화됨
  - 속성
    - `for="input태그의 id속성의 값"`

- \<div>태그

  - 태그들을 구분 짓고 나누기 위해 사용하는 태그. division의 약자.
  - 아무것도 나타내지 않고 그저 태그들을 구분 짓고 나누기 위해서 사용.

- \<select>태그

  - 여러 개의 선택지를 제시하고 싶을 때 씀
  - 하위 선택지에 해당하는 \<option>태그와 함께 사용!
  - 속성
    - \<select `name="gender"`> : \<input>태그의 name속성과 동일한 역할. \<select>태그가 반드시 가져야 하는 속성.
    - \<option `value="male"`> : \<input>태그에서 입력한 값과 동일한 역할. \<option>태그가 반드시 가져야 하는 속성.
    - _\<select>의 name속성과 \<option>의 value속성이 서로 짝을 이뤄 데이터로 전달됨!_

- \<textarea>태그

  - 한 번에 많은 글을 입력 받을 때 사용
  - 속성
    - \<textarea `cols="30"`> : 입력받을 글자 수만큼 키움
    - \<textarea `rows="10"`> : 입력받을 줄 수만큼 키움

- \<button>태그

  - \<input>태그의 버튼타입과 동일하게 버튼을 생성

    ```html
    <input type="button" value="회원 가입" />

    <button type="submit">회원 가입</button>
    ```

  - \<button>태그는 html요소를 \<button>태그 내에 담을 수 있기 때문에 매우 유용!

    ```html
    <button type="submit">
      <img src="강아지사진" />
    </button>
    ```
