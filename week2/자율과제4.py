players = ["황희조", "황희찬", "구자철", "이재성", "기성용"]
print("현재 경기 중인 선수:")
for i in players:
    print(i)
print("----------------------------------------------------")
a = int(input("OUT 시킬 선수 번호:"))
b = input("IN 할 선수 이름:")
print("----------------------------------------------------")

print("교체 결과:")
players.append(b)
del players[a]
for i in players:
    print(i)

