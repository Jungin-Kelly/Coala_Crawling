# pay = input("시급을 입력해주세요: " )
# pay = int(pay)
#
# if pay > 8350:
#     print("적절한 시급입니다:)")
# else:
#     print("최저시급보다 적어요:(")

numbers= [5 ,3, 7, 1, 9, 10,2]

for n in numbers:
    if (n>5) or (n<3):
        print(n)
    else:         #else -> 선택적인 애라 생략 가능
        print("5보다 작습니다.")

# 문자열 예시
articles = ["손흥민은 손으로 상대를 때렸다",
           "As로마의 니콜로 자니올로",
            "이강인의 팀 동려 페란 뭐시기"]
# for a in articles:
#     if "손흥민" in a:
#         print("손흥민 기사")
#     elif "이강민" in a:      #조건을 여러번 넣을 때 사용
#         print("이강민 기사")
#     elif "리콜로" in a:
#         print(1)
#     else:
#          print("손흥민/이강인이 나오지 않는 기사")

players = ["손흥민", "이강민", "황희찬"]
if "손흥" in players:    #in 다음에 리스트가 나오는 경우에는 정확하게 일치하는 값이 있어야함
    print(1)            # 위에꺼는 각 문자열 안에 해당 문자열이 포함되는 가를 묻는 거라서 ㄱㅊ
