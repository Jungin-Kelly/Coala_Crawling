string1 = "브이넥 라이트 다운 베스트"
string2 = "   25,900원   "

print(string1)
print(string2)

# 인덱싱
# print(string1[0])
# print(string1[1])
# print(string1[2])    #srting1[14]처럼 원래 가지고 있는 애보다 높은 인덱싱은 안됨
#                      crl + / => 전체 주석
# print(string1[-1])
# print(string1[-2])
# print(string1[-3])
# print(string1[-4])

# 슬라이싱 -> *앞엔 포함, 뒤에는 포함 x 주의의print(string1[0:3])       #앞에 번호는 포함, 뒤는 포함 x
# print(string1[4:7])
# print(string1[-3:-1])
# print(string1[:5])
# print(string1[8:])
# print(string1[:])

# 문자열 변환함수 replace
# print(string1.replace("라이트", "해비"))
# print(string1)
# string1 = string1.replace("라이트", "해비")
# print(string1)

# 공백 제거 함수
# print(string2.strip())
# print(string2)
# string2 = string2.strip()
# print(string2)

# string2 = string2.replace(",", "")
# print(string2)
# string2 = string2[:-1]
# print(string2)
string2 = string2.strip().replace(",", "").replace("원","")
print(string2)
# plusone = int(string2) + 1
# print(plusone)
