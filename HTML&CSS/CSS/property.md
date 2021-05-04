# 텍스트(폰트)와 관련된 프로퍼티

## font-size

## font-family

- 원하는 폰트의 종류 지정
- 한 단어로 된 폰트명은 따옴표 없이 사용가능
- 두 단어나 하이픈(-)으로 연결된 폰트명은 따옴표를 사용해서 한 폰트명임을 명시해야 함
- 여러 개 동시 지정하여 차례로 존재하는 폰트를 적용하는 방식
- 항상 마지막에는 모든 OS와 브라우저에 기본적으로 설치된 '일반 글꼴'을 둠
  - 일반 글꼴(폰트) : serif, sans-serif, cursive, fantasy, monospace 등
  - 웹 폰트 : 링크를 통해서 쉽게 폰트를 불러오는 방식

## font-style

- bold나 italic 적용하는 속성
- `: normal` : 기본 값, 기본 글자체
- `: italic` : 이탤릭체가 디자인되어 있는 폰트에서 사용
- `: oblique` : 무조건 글자를 기울여서 표현 (이탤릭체가 디자인되어 있지 않은 폰트에서 사용)

## font-weight

- 폰트 굵기를 지정할 때 사용
- `: bold`
- `: 100 ~ 900` : 400 - normal , 700 - bold

## font 프로퍼티

- font 프로퍼티 하나만으로도 위 네 개를 동시에 적용할 수 있다! (띄어쓰기로 구분)

# 텍스트 정렬과 관련된 속성

## text-align

- 텍스트 좌, 우, 중앙 정렬
- : left, center, right

## line-height

- 문장 사이의 간격을 조정함
- normal, 24px, 2 - 단위가 없는 숫자 값은 해당 요소의 폰트 사이즈를 기준으로 배로 만들어줌.
- line 간의 height가 아니라 'line의 height'임!

## letter-spacing

- 글자와 글자 사이의 간격을 조정함. 자간

## text-indent

- 문단의 시작부에 들여쓰기를 함
