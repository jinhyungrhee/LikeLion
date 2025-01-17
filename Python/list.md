# 자료형 - 리스트, 튜플, 딕셔너리

- 해당 자료형이 등장한 이유
- 어떤 상황에서, 어떤 방법으로, 어떤 데이터들을 관리할 것인가

## 리스트

- 산발적으로 흩어진, **변할 수도 있는** 데이터들을 **나란히** 묶어주는 자료형
  - 문자열도 "나란히"임! (덧, 곱, 인덱싱, 슬라이싱)
  - 리스트 다루기(리스트는 문자열의 친구)
    1. 리스트의 곱셈  
       `[1,2,3] * 3 == [1,2,3,1,2,3,1,2,3]`
    2. 리스트의 덧셈  
       `[1,2,3] \+ [4,5,6] == [1,2,3,4,5,6]`
    3. 리스트의 인덱싱
       ```
        list = [1,2,3]
        list[0] == 1
        list[1] == 2
        list[2] == 3
       ```
    4. 리스트의 슬라이싱
       ```
       list = [1,2,3]
       list[0:2] == [1,2]
       ```

## 튜플

- **변할 수 없는(변하면 안 되는)** 데이터들을 나란히 묶어주는 자료형
  - 리스트는 '대괄호', 튜플은 '소괄호' 사용
  - 사용하는 방법은 리스트와 완벽하게 동일!

## 딕셔너리(=해쉬)

- **대응**이 되는 데이터를 표현해주는 자료형
- '딕셔너리'는 각각의 키워드(탐색의 기준)를 통해 대응되는 단어를 찾을 수 있음
  - 탐색의 기준(키워드) = `key`
  - 탐색의 기준에 대응되는 찾고자 하는 값 = `value`
    ```
    {key1: value1, key2: value2, ...}
    ```
    - key는 중복되어서도, 변해서도 안 된다
