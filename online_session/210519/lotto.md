# python random 모듈

```py
from random import *

i = randit(1, 100) # 1부터 100사이의 임의의 정수
print(i)

f = random() # 0부터 1 사이의 임의의 float
print(f)

f = uniform(1.0, 36.5) # 1부터 36.5 사이의 임의의 float
print(f)

i = randrange(1, 101, 2) # 1부터 100 사이의 임의의 짝수
print(i)

i = randrange(10) # 0부터 9사이의 임의의 정수
print(i)

```

## randint()

- randint(최소, 최대) : 입력 파라미터인 최소와 최대 사이의 임의의 정수를 리턴

## random()

- random() : 0부터 1 사이의 부동소수점(float)숫자를 리턴

## uniform()

- uniform(최소, 최대) : 입력 파라미터인 최소와 최대 사이의 임의의 부동소수점(float)숫자를 리턴

## randrange()

- randrange(시작, 끝, \[간격\]) : 입력 파라미터인 시작부터 끝까지 (지정괸 간격으로 나열된) 숫자 중 임의의 정수를 리턴
