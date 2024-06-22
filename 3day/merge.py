# 원본 파일 열기
orginFile = open("c:\\tmp\\a.bmp", "rb")

# 합쳐줄 파일을 열어준다
mergeFile = open("c:\\tmp\\test.txt", "rb")


# 새로 생성할 파일을 열어준다
resultFile = open("c:\\tmp\\result.bmp", "wb")


# 원본파일을 새로생성할 파일에 쓰기한다
resultFile.write(orginFile.read())


# 합쳐줄 파일을 이어서 쓰기 한다
resultFile.write(mergeFile.read())

# 모든 파일을 닫아준다
orginFile.close()
mergeFile.close()
resultFile.close()