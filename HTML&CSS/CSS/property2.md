# 위치와 관련된 프로퍼티

## display

- 요소가 보여지는 방식을 지정
- HTML 요소
  1. display: `block`;
     - 항상 새로운 줄에서 시작
     - width: 100%
     - \<div>, \<h1>~\<h6>, \<p>, \<header>, \<section> 등
     - width, height, margin, padding 가능
  2. display: `inline`;
     - 새로운 줄에서 시작X
     - 필요한 만큼(요소의 content크기 만큼)만 의 너비만 가짐
     - \<a>, \<span>, \<img> 등
     - width, height, margin-top, margin-bottom **불가능** (양 옆으로는 적용됨)
  3. display: `inline-block`;
     - block과 inline요소의 특징을 모두 가짐
     - inline에서 불가능했던 width, height, margin-top, margin-bottom **가능**!
  4. display: `none`;
     - 아예 브라우저에 출력이 되지 않도록 하는 것

## position

- 요소의 위치를 정의
- 요소를 움직여서 배치할 수 있음
- `body {margin: 0;}` -> 기본 브라우저의 css 값 초기화

1. position: static;

   - 기본값
   - 좌표 프로퍼티를 쓸 수 없음

2. position: relative;

   - 상대 위치
   - 기본 위치(원래 static일 때 있어야 할 위치)를 기준으로 좌표를 사용함
   - width, height 값이 없을 때 원래(\<div>)처럼 **block요소**로 작용

3. poisition: absolute;

   - 절대 위치
   - 부모나 조상 중 relative, absolute, fixed가 선언된 곳을 기준으로 좌표 프로퍼티 적용
     - 만약 부모나 조상 프로퍼티에 relative, absolute, fixed가 없다면  
       최상단인 body 태그를 기준으로 위치가 지정됨!
   - width, height 값이 없을 때 원래(\<div>)처럼 block요소로 작용하지 않고 **inline요소**로 작용!
     - width와 height 값을 주면 정상적으로 적용됨
     - 다만 값이 없을 땐 너비(width)만 inline처럼 딱 붙게 되는 것 = **inline-block**과 동일!

4. poisition: fixed;

   - 보이는 화면을 기준으로 좌표 프로퍼티를 이용하여 위치를 고정
   - 스크롤할 때마다 따라다니는 메뉴가 이를 활용한 것

## z-index

- 숫자 값이 클수록 전면에 출현하게 됨 - ex) 1층, 2층
- static을 제외한 요소에서 사용

## flexbox

- 크기가 불분명한 요소들에 대해서도 효율적으로 동작
- 특별한 계산없이 쉽게 정렬 가능
- **핵심**  
   : **가로 혹은 세로의 정해진 방향을 기준으로 프로퍼티를 정렬**
- 구성

  1.  flex container(부모요소) - 정렬하고자 하는 부모요소에 `display: flex;` 추가

      - `flex-direction` : flex컨테이너 안의 item들의 방향을 정함

        - flex-direction: row; (_기본_, 왼→오)
        - flex-direction: row-reverse (오→왼);
        - flex-direction: column(위→아래);
        - flex-direction: column-reverse(아래→위);

      - `flex-wrap` : flex아이템이 flex 컨테이너를 벗어났을 때 줄을 바꾸는 속성

        - flex-wrap: nowrap; (_기본_, 줄을 바꿔주지 않음)
        - flex-wrap: wrap; (줄을 바꿔주는 속성)
        - **flex-flow**: row wrap; = flex-direction: row; + flex-wrap: wrap; (한꺼번에 사용 가능)

      - `justify-content` : **flex-direction**으로 정해진 방향(row/column)을 기준으로 **수평**으로 item을 정렬하는 방법을 정함 (row면 좌우, column이면 위아래)
        - justify-content: flex-start;(기본값, 왼쪽/위 정렬)
        - justify-content: center; (가운데 정렬)
        - justify-content: flex-end; (오른쪽/아래 정렬)
        - justify-content: space-around; (시작과 끝에 아이템을 하나씩 두고 그 사이에 남은 공간을 동일한 간격으로 하여 아이템을 배치)
        - justify-content: space-between; (시작과 끝을 기준으로 동일한 간격으로 아이템을 배치)
      - `align-items` : **flex-direction**으로 정해진 방향(row/column)을 기준으로 **수직**으로 item을 정렬하는 방법을 정함 (row면 위아래, column이면 좌우)
        - align-itmes: strecth; (기본값, 크기 지정이 없는 경우 item을 늘려서 맞춤)
        - align-itmes: flex-start; (위/왼쪽 정렬)
        - align-itmes: flex-end; (아래/오른쪽 정렬)
        - align-itmes: center; (가운데 정렬)
        - align-itmes: **baseline**; (content 안의 글꼴의 기준선을 기준으로 해서 정렬)
      - `align-content` : flex-direction으로 정해진 방향을 기준으로 수직으로 **여러 줄인** item을 정렬하는 방법을 정함
        - align-content: strecth; (기본값, 크기 지정이 없는 경우 item을 늘려서 맞춤)
        - align-content: flex-start; (위/왼쪽 정렬)
        - align-content: flex-end; (아래/오른쪽 정렬)
        - align-content: center; (가운데 정렬)
        - align-content: space-between; (끝에 딱 붙임)
        - align-content: space-around; (끝에도 동일한 간격 적용)

  2.  flex item(자식요소) - `display: flex;`가 적용된 부모요소의 자식요소들에만 사용 가능!

      - `flex-grow` : flex아이템의 확장과 관련된 속성, 기본 0

        - 0 : flex컨테이너가 커져도 flex아이템의 크기는 커지지 않음
        - 1이상의 값 : 해당 값에 따라 flex컨테이너를 채우기 위해 flex아이템이 커짐

      - `flex-shrink` : flex아이템의 축소와 관련된 속성, 기본 1
        - 0 : flex컨테이너의 크기가 flex아이템의 크기보다 작아져도 item의 크기가 줄어들지 않고 원래 크기를 유지함
        - 1이상의 값: flex컨테이너의 크기가 작아질 때 flex아이템의 크기가 flex컨테이너 크기에 맞춰서 줄어듦
      - `flex-basis` : flex아이템의 기본 크기를 결정함, 기본 auto
        - **단위**(px, %) 반드시 써줘야 함!!!
      - `flex` : flex-grow, flex-shrink, flex-basis의 축약형
        - 1 - on, 0 - off라고 생각하면 쉽다
        - **flex: 1;** ➡ flex-grow: 1; + flex-shrink: 1; (**둘 다 적용**한 상태)

## 간단한 레이아웃 제작

- 실제로는 선택자 중복 사용X

```
<style>
* {box-sizing: border-box;} // 레이아웃 편하게 보기
body {margin: 0;}           // 브라우저의 default margin 삭제
a {text-decoration: none;}  // 링크 밑줄 삭제 (글자 꾸미는 것 없앰)
a:link, a:visited, a:active {color: inherit}; // 상속받아서 글자 적용되도록 함 (수도 클래스 선택자)

 ...

html, body {
   height: 100%; // 전제 조건
}
body {
   display: flex;
   flex-direction: column; // <body>안에 있는 것들이 column방향으로 전체 정렬됨
}
#main {
   flex: 1; // height가 100%일 때, flex: 1;을 하면 flex-grow가 적용됨
}
.footer{
   flex-shrink: 0; // 사이트가 줄어도 footer의 크기가 작아지지 않도록 고정
}

</style>
```

➡ flex의 등장으로 sticky footer의 구현이 쉬워짐!
