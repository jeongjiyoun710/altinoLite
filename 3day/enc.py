import os


# 바이트를 1바이트 증가시켜주는 함수
def increment_bytes(input_bytes):
    byte_array = bytearray(input_bytes)
    for i in range(len(byte_array)):
        byte_array[i] = (byte_array[i]+1) % 256
    return bytes(byte_array)


# 원본 이미지를 열어준다
originFile = open("c:\\tmp\\a.bmp", "rb")

# 숨길 데이터 파일을 열어준다
secretFile = open("c:\\tmp\\test.txt", "rb")

# 숨겨진 이미지를 저장하여 새로 생성할 파일을 열어준다
resultFile = open("c:\\tmp\\result.bmp", "wb")

# 원본이미지와 숨길 데이터파일의 사이즈를 각각 구해온다
originSize = os.path.getsize("c:\\tmp\\a.bmp")
secretSize = os.path.getsize("c:\\tmp\\test.txt")
# 원본 이미지에서 54바이트만큼 새로 생성할 파일에 복사해준다
originData = originFile.read(54)
resultFile.write(originData)

# 원본 이미지의 파일이 끝날 때까지 계속 1바이트씩 읽어서 숨겨진 이미지에 복사한다
while originData:
    # 단! 숨길 데이터의 1바이트를 원본이미지의 8바이트 속에 숨겨서 숨겨진 이미지에 복사한다
    while secretSize>=0:
        byteData = secretFile.read(1)
        intData = int.from_bytes(byteData)

        buffer = [None]*8
        col = 7
        while col>=0:
            buffer[col] = intData%2
            intData//=2
            col -= 1

        for i in range(0,8):
            originData = originFile.read(1)
            originIntData = int.from_bytes(originData)

            if(originIntData % 2 != buffer[i]) :
                originData = increment_bytes(originData)

            resultFile.write(originData)
        
        secretSize -= 1
    # 더이상 숨길 데이터가 없으면 원본 이미지 남은 부분을 그대로 복사해준다
    originData = originFile.read(1)
    resultFile.write(originData)

# 열었던 파일을 닫아준다
originFile.close()
secretFile.close()
resultFile.close()