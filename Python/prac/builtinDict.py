# 딕셔너리 (내장함수)

pairs = {'잔나비': '뜨거운 여름밤은 가고 남은 건 볼품없지만', '소히': '산책', '홍크': '어쩌면'}

# 하나의 key-value 쌍을 더 추가하는 방법
# 딕셔너리변수[새로운 key] = 새로운 value

print(pairs)
pairs['스탠딩 에그'] = '휴식'
print(pairs)

# 특정 key-value 삭제하는 방법
# del 딕셔너리변수[key]
# del()은 리스트나 튜플에서도 특정 인덱스의 요소를 삭제할 때 사용!

print(pairs)
del pairs['잔나비']
print(pairs)

# key로 value 얻기
# 딕셔너리변수.get(key) --> 찾고자하는 key에 "대응"되는 값(value)을 return해줌

v = pairs.get('소히')
print(v)
