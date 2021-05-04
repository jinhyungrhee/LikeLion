# 박스 모델 개념

## Content(내용)

- 이미지나 텍스트 같이 우리가 태그 사이에 담은 **실제 내용**을 담고 있는 부분
- width와 height 사용

## Border(경계선)

- content(내용)을 감싸고 있는 **테두리**
- 프로퍼티
  - border-style
  - border-width
  - border-color
- border 프로퍼티로 한꺼번에 처리 가능
- border-radius : 경계선을 둥글게 표현
  - border-top-left-radius
  - border-top-right-radius
  - border-bottom-left-radius
  - border-bottom-right-radius
    - 모서리에 들어가는 원의 반지름의 길이로 적용(px)
    - 모서리에 들어가는 원을 타원형으로도 적용 가능  
      → border-top-left-radius: 30px 10px; (가로 반지름이 30px 세로 반지름이 10px인 타원)
    - '/'를 이용해서 한 번에 적용 가능

## Padding(패딩)

- Content(내용)와 Border(경계선) 사이의 **여백**
- Border(경계선) 내부의 여백
- 네 방향 따로 적용 가능
- 배경색을 지정하면 Padding까지 포함됨

## Margin(마진)

- Border(경계선) 밖의 **여백**
- Border(경계선) 외부의 여백
- 네 방향 따로 적용 가능
- 위 아래 다른 요소에서 마진을 적용하면 두 마진이 함께 공존하지 않음.  
  마진 상쇄(Margin Collapse)에 의해서 상하 요소 사이의 마진은 서로 상쇄가 됨.  
  기준은 큰 쪽 마진.

=> **적용하는 값의 개수에 따라서 적용되는 위치가 달라짐**

- 띄어쓰기로 구분
- 상, 우, 하, 좌 순서(시계방향)

## box-sizing

- 박스 전체 크기의 기준을 정하는 프로퍼티
- `: content-box;` : 기본값
  - width(height) = content size
- `: border-box;` : border의 두께까지 포함된 크기를 전체 크기로 지정
  - width(height) = content size + padding + border
