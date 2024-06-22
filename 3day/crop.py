# 원본 파일을 열어준다
originFile = open("c:\\tmp\\result.bmp", "rb")
# 새로만들 파일을 열어준다
cropFile = open("c:\\tmp\\test.txt", "wb")

# 원본파일에서 합쳐진 파일의 크기만큼 읽어 새로만들 파일에 써준다
# 원본파일의 크기는 6750054이고 합쳐진 파일 크기는 알 수 없다
# 코드를 완성해라
originFile.read(6750054)
cropFile.write(originFile.read())

# 파일을 닫아준다
originFile.close()
cropFile.close()