import random

# 변수 생성
a = random.randint(1, 9)
b = random.randint(1, 9)

# 정답
gugudan = a * b

print("구구단을 외자 !")
print(a,"*",b,"= ?")


# 답 입력
user = float(input("답 >>"))

# 확인
if(user == gugudan) :
    print("정답입니다!")
else :
    print("이걸 틀리냐 ㅋ")