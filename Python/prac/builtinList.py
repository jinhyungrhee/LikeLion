# 리스트(내장함수)

li = [3, 1, '배가', 4, '고파요', 5, 1]
li2 = [3, 1, 4, 5, 2]

# 인덱싱

print(li[2])  # 배가

# 슬라이싱

print(li[0:3])  # [3, 1, '배가']

# 내장함수

# len('리스트변수') : 리스트의 길이
print(len(li))  # 7

# sort() : 리스트 원소를 '오름차순'으로 정렬
# 주의 - sort()는 정렬된 리스트를 반환하지 않음!!
print(li2)  # [3,1,4,5,2]
li2.sort()
print(li2)  # [1,2,3,4,5]

# index() : 리스트 내의 특정 원소의 인덱스 반환
print(li.index('배가'))  # 2

# count() : 리스트 내의 특정 원소의 개수 세기
print(li.count(1))  # 2