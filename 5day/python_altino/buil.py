from ast import Global
from AltinoLite import *


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
    if(r4Avr > 100):
        turnDeg = (-r4Avr)+100
        if(turnDeg > 127 or turnDeg < -127):
            # print("127 넘음")
            Steering(-127)
        else:
            Steering(turnDeg)

    # 아무것도 아닌경우 다시 직진
    elif(r4Avr < 100 and l5Avr < 100):
        Steering(0)

    # 좌측으로 붙는 경우 오른쪽으로
    elif(l5Avr > 100):
        # Steering(l5Avr-600)
        turnDeg = l5Avr-100
        if(turnDeg > 127 or turnDeg < -127):
            # print("127 넘음")
            Steering(127)
        else:
            Steering(turnDeg)



def go_turn():
    Gear()
    global turnDeg
    # 멈춤
    if(f1Avr > 40 and f2Avr > 100 and f3Avr > 40):
        Go(0, 0)

    # 아무 상황도 아닐 경우
    else:
        Steering(0)


    # 다음부터는 직진상태에서 커브
    # 오른쪽으로
    if(f1Avr > 5 and f2Avr > 5 ):
        turnDeg = f1Avr-5
        Steering(turnDeg)
        delay(300)
    elif(f1Avr > 5 and l5Avr > 50):
        turnDeg = (f1Avr-5)+(l5Avr-50)

        # 최대치 확인
        if(turnDeg > 127 or turnDeg < -127):
            Steering(127)
            delay(300)
        else:
            Steering(turnDeg)
            delay(300)

    # 왼쪽으로
    elif(f2Avr > 5 and f3Avr > 5):
        turnDeg = (-f3Avr)+5
        Steering(turnDeg)
        delay(300)
    elif(f3Avr > 5 and r4Avr > 50):
        turnDeg = (-f3Avr+5)+(-r4Avr+50)

        # 최대치 확인
        if(turnDeg > 127 or turnDeg < -127):
            Steering(-127)
            delay(300)
        else:
            Steering(turnDeg)
            delay(300)




Open()

IRSet()


while 1:
    Go(300, 300)
    Turn()
    go_turn()
    delay(100)
    


Close()