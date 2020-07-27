# 리스트 -> 일일이 변수 만들어 줄 필요 없음
players = ["황희조","황희찬" ,"구자철", "이재성", "기성용"]
print(players)
print(players[1])

players.append("이승우")
print(players)
players.append("김민재")
print(players)

del players[1]
print(players)

del players[1]
print(players)

print(len(players))
print(len(players[0])) #정확한 인덱스를 말하면 그 값의 길이를 알려줌