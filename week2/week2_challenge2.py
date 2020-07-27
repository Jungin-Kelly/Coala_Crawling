data = ["조회수: 1,500", "조회수: 1,002", "조회수: 300", "조회수: 251", "조회수: 13,432", "조회수: 998"]
for d in data:
    print(d)
for d in data:
    d = d[5:]
    d = d.replace(",","")
    print(d)
sum = 0                   #sum을 안에 두게 되면 매번 0으로 돌아옴
for i in range(len(data)): #얘는 d로 받는 거지 list data 얘 자체를 바꾸는게 아님
    d = data[i][5:]
    d = d.replace(",","")
    sum = sum + int(d)

for i in range(len(data)):   #list data 안에 내용물 자체를 바꾸려면 이렇게 해야함.
    data[i] = data[i][5:]
    data[i] = int(data[i].replace(",",""))
    sum = sum + data[i]
print(data)
print(sum)
