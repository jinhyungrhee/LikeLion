# CSS 기초

## CSS

- Cascading Style Sheets
- 웹에 적용할 스타일들을 명시해 놓은 일종의 스타일 명세서

## 선택자(Selector)

- 스타일을 적용하고자 하는 HTML 요소를 선택하는 역할

## 속성(Property)

- 지정할 스타일의 속성명에 해당
- `속성 : 값 ;`이 한 단위
- ;(세미 콜론)을 이용하여 구분

## 값(Value)

- 키워드나 특정 단위를 이용하여 원하는 스타일을 적용
- 속성(Property)와 쌍을 이룸

```css
p {
  font-family: '맑은 고딕';
  font-size: 18px;
  color: blue; // 선언(Declaration)
} // 선언블럭(Declaration Block)
```

# HTML에 CSS를 적용하는 방법

## Link Style

- HTML 외부에 있는 CSS 파일을 불러옴

## Embedding Style

- HTML의 \<head>에 \<style>을 이용하여 CSS를 작성

## Inline Style

- HTML요소에 직접 style 속성(Attributes)을 이용하여 CSS를 작성
