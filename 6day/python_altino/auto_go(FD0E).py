import speech_recognition as sr
from ast import Global
from AltinoLite import *
import pygame

# 음성인식 
def inputAudio():
    # 음성 인식기 인스턴스 생성
    recognizer = sr.Recognizer()

    # 마이크를 음성 소스로 사용
    with sr.Microphone() as source:
        print("말씀해 주세요...")
    
        # 잡음 수준을 자동으로 조정
        recognizer.adjust_for_ambient_noise(source)
    
        # 음성을 들음
        audio_data = recognizer.listen(source)
    
        try:
            # 음성을 텍스트로 변환 (한글 인식)
            text = recognizer.recognize_google(audio_data, language='ko-KR')
            print(f"인식된 텍스트: {text}")
        except sr.UnknownValueError:
            print("음성을 인식할 수 없습니다.")
        except sr.RequestError as e:
            print(f"구글 음성 인식 서비스에 문제가 있습니다: {e}")

    return text




# 음성 파일 재생
def Al_sound(soundFileName):
    print("사운드 파일 재생 : " + soundFileName)
    pygame.mixer.init()
    pygame.mixer.music.load("D:\\J.JiYoun\\mp3\\" + soundFileName)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

f1Sum = 0
f2Sum = 0
f3Sum = 0
r4Sum = 0
l5Sum = 0
b6Sum = 0


f1Avr = 0
f2Avr = 0
f3Avr = 0
r4Avr = 0
l5Avr = 0
b6Avr = 0

cnt = 1  #평균 카운트



# 바퀴 돌리는 각도 변수
turnDeg = 0 


# 센서 평균 구하기
def Gear():
    global f1Sum
    global f2Sum
    global f3Sum
    global r4Sum
    global l5Sum
    global b6Sum

    global f1Avr
    global f2Avr
    global f3Avr
    global r4Avr
    global l5Avr
    global b6Avr

    global cnt

    f1Sum += sensor.IR[1]
    f2Sum += sensor.IR[2]
    f3Sum += sensor.IR[3]
    r4Sum += sensor.IR[4]
    l5Sum += sensor.IR[5]
    b6Sum += sensor.IR[6]


    f1Avr = f1Sum // cnt
    f2Avr = f2Sum // cnt
    f3Avr = f3Sum // cnt
    r4Avr = r4Sum // cnt
    l5Avr = l5Sum // cnt
    b6Avr = b6Sum // cnt


    cnt+=1

    if cnt>3:
        cnt=1
        f1Sum = 0
        f2Sum = 0
        f3Sum = 0
        r4Sum = 0
        l5Sum = 0
        b6Sum = 0

    print(str(f1Avr) + " | " + str(f2Avr) + " | " + str(f3Avr) + " | " + str(r4Avr) + " | " + str(l5Avr) + " | " + str(b6Avr))


def Turn():
    Gear()

    global turnDeg

    # 우측으로 붙는 경우 왼쪽으로
    if(r4Avr > 150):
        turnDeg = (-r4Avr)+150
        if(turnDeg > 127 or turnDeg < -127):
            # print("127 넘음")
            Steering(-127)
        else:
            Steering(turnDeg)

    # 아무것도 아닌경우 다시 직진
    elif(r4Avr < 150 and l5Avr < 150):
        Steering(0)

    # 좌측으로 붙는 경우 오른쪽으로
    elif(l5Avr > 150):
        # Steering(l5Avr-600)
        turnDeg = l5Avr-150
        if(turnDeg > 127 or turnDeg < -127):
            # print("127 넘음")
            Steering(127)
        else:
            Steering(turnDeg)



def go_turn():
    Gear()
    global turnDeg
    # 멈춤
    if(f1Avr > 60 and f2Avr > 100 and f3Avr > 60):
        Go(0, 0)

    # 아무 상황도 아닐 경우
    else:
        Steering(0)


    # 다음부터는 직진상태에서 커브
    # 오른쪽으로
    if(f1Avr > 60 and f2Avr > 70 ):
        turnDeg = f1Avr-30
        Steering(turnDeg)
        delay(300)
    elif(f1Avr > 60 and l5Avr > 70):
        turnDeg = (f1Avr-60)+(l5Avr-70)

        # 최대치 확인
        if(turnDeg > 127 or turnDeg < -127):
            Steering(127)
            delay(300)
        else:
            Steering(turnDeg)
            delay(300)

    # 왼쪽으로
    elif(f2Avr > 60 and f3Avr > 70):
        turnDeg = (-f3Avr)+70
        Steering(turnDeg)
        delay(300)
    elif(f3Avr > 60 and r4Avr > 70):
        turnDeg = (-f3Avr+60)+(-r4Avr+70)

        # 최대치 확인
        if(turnDeg > 127 or turnDeg < -127):
            Steering(-127)
            delay(300)
        else:
            Steering(turnDeg)
            delay(300)


# 시작 음성
Al_sound("start.mp3")


# CDS 센서 작동 변수
cds_ok = False
cds_cnt = 0

Open()
Al_sound("conn.mp3")

IRSet()


Al_sound("go.mp3")
while 1:
    Go(260, 260)
    Turn()
    go_turn()
    if(sensor.CDS > 730 and cds_ok == False):
        Go(0, 0)
        Al_sound("stopQue.mp3")

        # 음성인식
        text = inputAudio()

        if (text == "출발"):
            print(sensor.CDS)
            cds_ok = True
            continue
        else:
            break

    cds_cnt+=1


    if(cds_cnt == 10):
        cds_ok = False
    
    delay(100)


Close()