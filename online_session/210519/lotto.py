#from random import *
import random


# 난수 생성 함수(보너스 번호 포함 7개)

def lotto_number():
    num_list = []

    for i in range(6):
        num = random.randint(1, 45)
        while num in num_list:
            num = random.randint(1, 45)
        num_list.append(num)

    bonus_num = random.randint(1, 45)
    while bonus_num in num_list:
        bonus_num = random.randint(1, 45)
    return num_list, bonus_num


# 추첨 번호를 출력해주는 함수

def print_lotto_number(lotto_num, bonus_num):
    print(lotto_num, end=' + ')
    print(bonus_num)


# 당첨 확인 함수

def check_number(user_num):
    num_count = 0  # 몇개의 번호가 일치하는지 count하기 위한 변수
    bonus_count = 0  # 보너스 번호 일치하는지 확인
    for num in user_num:
        if num in lotto_numbers:  # lotto_numbers는 전역변수
            num_count += 1
        if num == bonus_number:  # bonus_number도 전역변수
            bonus_count = 1

    if num_count == 6:
        print("1등")
    elif num_count == 5:
        if bonus_count == 1:  # 숫자 5개와 보너스 번호 일치
            print("2등")
        else:  # 숫자 5개만 일치
            print("3등")
    elif num_count == 4:
        print("4등")
    elif num_count == 3:
        print("5등")
    else:
        print("복권 하나 더 사!")


# main
lotto_numbers = []
bonus_number = 0

while(True):
    print("1. 로또 번호 추첨")
    print("2. 번호 당첨 확인")
    print("3. 종료")
    mode = int(input("실행할 번호 입력: "))
    if (mode == 1):
        lotto_numbers, bonus_number = lotto_number()
        print_lotto_number(lotto_numbers, bonus_number)

    elif (mode == 2):
        user_number = []
        for i in range(6):
            user_input = int(input("1 ~ 45 사이의 번호를 입력해주세요: "))
            user_number.append(user_input)
        check_number(user_number)

    elif (mode == 3):
        print("프로그램 종료")
        break
