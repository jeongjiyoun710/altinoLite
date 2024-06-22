# 사용자로부터 2진수를 입력받음
userNumber = input("1바이트 2진수를 입력하세요 (최대 8자리) : ")

# 사용자 입력 값검증
if(len(userNumber)>8):
    print("8자리보다 큰 2진수!")
    exit()


# 바이너리 저장
buffer = [None]*8


# 2진수를 buffer에 저장
cnt = 0

for i in userNumber.rjust(8,'0'):
    buffer[cnt] = i
    cnt+=1

print(buffer)


# 10진수 변환
result = 0


num = 128 #10진수로 변환할 때 사용하는 수

numCnt = 0 #인덱스

while num>0:
    # buffer의 numCnt인덱스에 값이 내려가는 num을 곱해서 나오는 값을 result에 더해서 저장
    result += int(buffer[numCnt]) * num

    # 저장된 값 확인 후, 다음 인덱스로 단계를 넘김
    print(num, buffer[numCnt], result)
    numCnt+=1
    num=num//2


print("10진수 : ",result)


