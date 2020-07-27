# Max = 10
# for i in range(1,Max):  #앞에 있는 숫자는 포함, 뒤는 포함 x
#     print(i)             # i 는 임시 변수, 다른 애가 들어가도 상관 없음
#     print("반복문을 배워봅시다.")

#for i in range(숫자1)  -> 숫자1 -1 까지 반복
#for i in range(숫자1,숫자2) -> 숫자1부터 숫자2 -1 까지 반복
#for i in range(숫자1,숫자2,숫자3) ->숫자 1 부터 숫자 2-1까지 반복하되, 숫자 3을 단위로

players = ["황희조","황희찬" ,"구자철", "이재성", "기성용"]
print("2019년 아시안컵 출전명단")
for i in range(len(players)):
    print(players[i])

print("명단 출력 끝")

for p in players:    #players에 있는 애들을 p로 받고 출력하겠음
    print(p)

print("명단 출력 끝")