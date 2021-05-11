# 상속과 우선순위

## 상속

- 부모나 조상 요소에 적용된 CSS 프로퍼티를 자식 혹은 후손 요소가 물려받는 것

- 모든 CSS 프로퍼티가 상속되는 것은 아님!

  - width, height, margin, padding, display 등 상속X
  - Full Property Table(https://www.w3.org/TR/CSS21/propidx.html)

- 상속되지 않는 프로퍼티를 상속받게 만들기 - 'inherit' 사용
  - margin: **inherit**;

## Cascading

- CSS 적용 우선순위 : 3가지 규칙

1. 중요도 : CSS가 어디에 선언되었는지에 따라 우선순위가 달라짐

   1. \<head> 태그 내의 \<style>태그
   2. \<head> 태그 내의 \<style>태그 내의 \@import문
   3. \<link> 태그로 연결된 CSS
   4. \<link> 태그로 연결된 CSS 내의 \@import
   5. 브라우저 디폴트 스타일시트

2. 명시도

   1. !important
   2. 인라인 스타일(inline style)
   3. 아이디 선택자(id selector)
   4. 클래스, 속성, 가상클래스 선택자(class, attribute, pseudo class selector)
   5. 태그 선택자(type selector)
   6. 전체 선택자(universal selector)
   7. 상속(inherit)

   - _id로 지정해 놓은 스타일이 있으면 class로 같은 스타일을 먹이려고 해도 적용되지 않음_(id가 우선이기 때문에 id선택자 기준으로 스타일 적용됨)

3. 선언 순서

   - 나중에 선언된 스타일이 우선 적용
