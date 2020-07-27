#csv -> 콤마로 자료 구분해주는 애
f = open("hitsong.csv","w",encoding='UTF-8') #엑셀 파일에서 깨지면 encoding='UTF-8' 이거 써주면됨
singers = ["박정현", "임창정", "아이유", "이즈"]
songs = ["꿈에","소주한잔","좋은날","응급실"]
for i in range(len(singers)):                   # singers의 길이 만큼 i번째 singers 에 i번째 song 을 더하고 엔터를 해줘
    f.write(singers[i] + ',' + songs[i] + '\n')
f.close()