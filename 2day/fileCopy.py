
# 파일 경로 찾기
myFileURL = str(input("원본 파일의 경로를 입력하세요 : "))

# 복사 과정
myFile = open(myFileURL, "r")

file1 = myFile.read()

myFile.close()


# 복사 파일 생성 준비
newFileURL = str(input("복사 파일의 저장 경로를 입력하세요 : "))

newFileName = str(input("복사 파일 이름을 입력하세요 : "))

# 생성 시작
newFile = open(newFileURL+"\\"+newFileName+".txt", "w")

newFile.write(file1)

newFile.close()
