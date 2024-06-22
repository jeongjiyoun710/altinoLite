import os

# 숨겨진 이미지를 열어준다
originFile = open("d:\\J.JiYoun\\python_class\\3day\\test\\enc.bmp", "rb")

# 숨겨진 요소를 저장하여 새로 생성할 파일을 열어준다
resultFile = open("d:\\J.JiYoun\\python_class\\3day\\test\\result.txt", "wb")

# 임시 저장소
buffer = ""
# 54바이트 버리기
originFile.read(54)

# 이후 8비트에 하나씩 총 171비트가 모일때까지 꺼내서 저장하기
cnt = 0 # 171이 될때까지 while에 사용
now = 0 # 바이트 안에 몇번째 비트에 사용

while cnt<171:
    print("while 실행")
    for i in range(0, 8):
        if(i == 7):
            buffer += str(originFile.read(1))
            # print(originFile.read(1))
        else:
            originFile.read(1)
    
    cnt+=1

print(buffer)
resultFile.write(buffer)

# 파일 닫기
originFile.close()
resultFile.close()
    
