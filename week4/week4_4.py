# openptxl 연습하기
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active # 현재 활성화 돼 있는 엑셀파일의 시트
sheet['A1']= "hello world" #이건 셀 번호를 정확히 알이야함
sheet.cell(row=3,column=3).value="goodbye" #3열 3행에 value값을 넣어줘/ 반복문에 유리
sheet.append(["python", "java", "html", "javascript"]) # 지금 열려있는 엑셀 파일의 가장 아래 행에 자료를 추가해 준다
sheet.append(["코알라","스터디","크롤링"])  #행 별로 데이터 추가하는 경우가 많아서 append 가장 많이 사용
wb.save("test.xlsx")
