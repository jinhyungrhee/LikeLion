text = """케로케로 케로케로 힘차게 케로 케로 케로 나가자
우리 앞에 있는 모든 시련들 겁낼 필요 없다
케로로 소대 오늘도 출동을 하네
큰맘먹고 세차하면 비오고 소풍가면 소나기
급하게 탄 버스 방향 틀리고
건널목에 가면 항상 내 앞에서 빨간불
케로케로 케로케로 힘차게 케로케로케로 나가자
우리 앞에 있는 모든 시련들 겁낼 필요 없다
다섯 개구리 모여서 공명을 하네
힘들어도 밝은 얼굴 웃어봐 우린 내일이 있어
세상 일이 힘이 들고 지쳐도
우리 모두 모여 하나 되면 해낼 수 있어
이 세상에 두려운 건 없어 너와 함께면!"""

textList = text.split()
print(textList)

wordDict = {}

for word in textList:
    if word in wordDict:  # word가 wordDict안에 있으면
        wordDict[word] += 1  # 같은 이름에 개수 1 추가
    else:  # 없으면
        wordDict[word] = 1  # 개수를 1로 만듦 (있다는 것만 표시)

print(wordDict)
