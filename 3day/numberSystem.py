userNumber = int(input("0~255 사이의 숫자를 입력하세요 : "))

# 입력값 검출
if(userNumber>255 or userNumber<0):
    print("입력한 값이 0~255 사이의 숫자가 아닙니다")
    exit()


# 바이너리를 저장할 저장공간 할당
buffer = [None] * 8

# 2진수로 변환
cnt = 7

while cnt>=0:

    buffer[cnt] = userNumber % 2
    userNumber = userNumber//2

    cnt-=1


# 출력
print(buffer)