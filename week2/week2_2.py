# 입력 연습하기
name = input("이름을 입력해주세요: ")
age = input("나이를 입력해주세요: ")  # input으로 받은 값은 str로 인식됨
age = int(age)  #형 변환

print("이름은", name)
print("나이는", age)

g_age = age -1
print("만 나이는", g_age)