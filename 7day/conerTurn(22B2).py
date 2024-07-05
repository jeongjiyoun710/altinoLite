from AltinoLite import *


# 완곡한 코너를 만났을 때, 빈 칸으로 꺾어야한다. 즉, 벽이 있다가 없어지는 구간을 찾아서 회전해야하는 것이다

# chap.1 : 길가다 빈공간 찾기
# chap.2 : 빈공간으로 꺾기
# chap.3 : 만약 부딪힐 것 같으면 다시 뒤로

# 회전해야하는지 확인
turnCheck = False

# 빈 방향 확인 변수
leftConer = False
rightConer = False

forwardClose = False  # 앞이 막혔나 확인

# 앞&양쪽 거리
f2 = 0
l5 = 0
r4 = 0

# 코너 만나는 것을 확인하는 함수
def conerCheck():
    global l5
    global r4
    global f2
    global leftConer
    global rightConer
    global forwardClose

    f2 = sensor.IR[2]
    r4 = sensor.IR[4]
    l5 = sensor.IR[5]

    # 초기화 및 설정 (코너 확인)
    if(l5 != 0):
        leftConer = False
    elif(r4 != 0):
        rightConer = False

    if(l5 == 0):
        leftConer = True
        forwardCloseCheck()
    elif(r4 == 0):
        rightConer = True
        forwardCloseCheck()



# 코너 체크가 되었다면, 앞이 막혔는지 확인하는 함수
def forwardCloseCheck():
    global f2

    global forwardClose

    global leftConer
    global rightConer

    global turnCheck

    if(f2 >= 150):
        Go(0, 0)

        turnCheck = True
        
        # 멈춘 후, 빈 방향으로 꺾기 함수 실행
        if(leftConer == True):
            while turnCheck:
                conerTurn("left")
                
        elif(rightConer == True):
            while turnCheck:
                conerTurn("right")



# 이제 코너를 도는 함수이다
# 이 함수에서는 받아온 값이 만약 left라면 왼쪽으로 가는 명령을, right라면 오른쪽으로 가는 명령을 내릴 것이다
# 회전 중, 만약 대각선 센서를 통해 벽과 부딪히는 것을 감지하면 뒤로 다시 빠진다.
# 다만, 뒤로 빠질 경우, 지금 회전하는 반대 방향으로 회전하며 뒤로 간다.
# 뒤 센서가 감지할 경우 다시 앞으로 간다.

def conerTurn(result):
    turnValue = 0
    
    # 오른쪽 or 왼쪽
    if(result == "left"):
        turnValue = -127
    elif(result == "right"):
        turnValue = 127

    print(result)
    # ----------------------------------

    # 회전이동 시작
    # 벽에 부딪히는지 확인
    f1 = 0
    global f2
    f3 = 0
    f1Check = False
    f3Check = False


    b6 = 0 # 뒤 센서

    # 다 돌았을 경우 초기화할 변수들
    global leftConer
    global rightConer
    global forwardClose

    f1 = sensor.IR[1]
    f2 = sensor.IR[2]
    f3 = sensor.IR[3]

    # 지금부터는 뒤로 다시 돌아가는 것 ====================

    # 뒤로 다시 회전 초기 설정
    if(f1 >= 150):
        f1Check = True
    elif(f3 >= 150):
        f3Check = True


    # 회전하며 이동하자 (뒤로)
    # 먼저 뒤에 부딪히는지 확인
    if(b6>=300):
        Go(0, 0)
        f1Check = False
        f3Check = False
    elif(f1Check == True):
        Steering(-30) # 왼쪽으로 핸들
        Go(-270, -270)
    elif(f3Check == True):
        Steering(30) # 오른쪽으로 핸들
        Go(-270, -270)

    # 아무것도 해당하지 않을 경우
    else:
        Steering(turnValue)
        Go(270, 270)

    
    # 만약 다 돌았을 경우 => f1,2,3 센서가 아무것도 감지하지 않을 경우
    if(f1 == 0 and f2 == 0 and f3 == 0):
        global turnCheck

        turnCheck = False
        print("회전 종료")
        Steering(0)


    
    

# 시작
Open()

IRSet()

Go(270, 270)
while 1:
    # print(str(sensor.IR[4]) + "||" + str(sensor.IR[5]))
    conerCheck()

    print("앞왼쪽 :" + str(sensor.IR[1]) + " | 앞 :" + str(sensor.IR[2]) + " | 앞오른쪽 :" + str(sensor.IR[3]) + " | 오른쪽 :" + str(sensor.IR[4]) + " | 왼쪽 :" + str(sensor.IR[5]) + " | 뒤 :" + str(sensor.IR[6]))
    



Close()