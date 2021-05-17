# 제어문 - 분기문
# if(조건):

# 예제1 : 85점 이상이면 pass 이하면 fail

'''
score = int(input("점수를 입력해 주세요: "))

if(score >= 85):
    print("PASS")
else:
    print("FAIL")
'''

# 예제2
'''
activity = input("너 동아리 뭐해?: ")

if(activity == "멋쟁이사자처럼"):
    print("어, 너도 멋사야?")
else:
    print("....그래")
'''

# 예제3 : 비교 조건이 3개 이상인 경우
# 5000이상 : 아웃백 / 3000이상 : 학식 / 1000이상 : 컵라면 / ㅠㅠ: 공기밥

money = int(input("돈 얼마 있어?: "))

'''
if(money >= 5000):
    print("아웃백 가자")
else:
    if(money >= 3000):
        print("학식 먹자")
    else:
        if(money >= 1000):
            print("컵라면 먹자")
        else:
            print("공기밥 가즈아ㅏㅏㅏㅏㅏ")
'''
# else if == elif

if(money >= 5000):
    print("아웃백 가자")
elif(money >= 3000):
    print("학식 먹자")
elif(money >= 1000):
    print("컵라면 먹자")
else:
    print("공기밥 가즈아")
