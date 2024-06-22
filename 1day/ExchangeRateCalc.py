

now = float(input("현재 원화 환율 (1달러)을 입력하세요 : "))
hope = int(input("희망하시는 환전 금액(원)을 입력하세요 : "))

final = hope/now

print("환전 금액은'"+str(round(final, 2))+"'달러 입니다")
