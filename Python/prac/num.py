# 주석 = 메모
print("안녕하세요")
# 우리 사용자들만 읽을 수 있게 작성한 것

# 숫자형 - 정수형 / 실수형

# 정수형 - int(integer),  실수형 - float(floating point)

num1 = int(input("여기에 첫번째 정수를 입력하세요 : "))
num2 = int(input("여기에 두번째 정수를 입력하세요 : "))

print(num1 + num2)

# 나눗셈 - 실생활에서는 몫을 위한 나눗셈을 함 / 컴퓨터에서는 몫과 나머지 둘 다 중요함

# '몫'을 구하는 연산자 : //
# '나머지'를 구하는 연산자 : %
# 몫 + 나머지를 함께 구하는 연산자 : /

print(num1//num2)  # 몫
print(num1 % num2)  # 나머지
print(num1/num2)  # 몫 + 나머지

# 거듭제곱(**) : 밑**승수
print(num1**num2)
