from AltinoLite import *
from ast import Global


# 왼쪽이 비었다가 뒤가 막히면 이후 왼쪽으로 턴
# 왼쪽이 비었다가 앞이 막히면 이후 왼쪽으로 후진/턴

# 오른쪽이 비었다가 뒤가 막히면 이후 오른쪽으로 턴
# 오른쪽이 비었다가 앞이 막히면 이후 오른쪽으로 후진/턴

leftEmpty = False
leftAfterBlock = False
rightEmpty = False
rightAfterBlock = False

# 벽 감지 후 얼마나 뒤로 가는지 저장
right_detectBack = 0
left_detectBack = 0

Open()
IRSet()

def rotate():
    global leftEmpty
    global leftAfterBlock
    global rightEmpty
    global rightAfterBlock
    global left_detectBack
    global right_detectBack

    if(sensor.IR[5] == 0):
        leftEmpty = True
    elif(sensor.IR[4] == 0):
        rightEmpty = True


    # 이후 감지
    if(leftEmpty == True and sensor.IR[5] >= 5):
        leftAfterBlock = True
        leftEmpty = False
    elif(rightEmpty == True and sensor.IR[4] >= 5):
        rightAfterBlock = True
        rightEmpty = False

    # 만약 빈것을 확인 후 다시 감지가 된 상태라면, 얼마나 뒤로 가는지 저장
    if(leftAfterBlock == True and sensor.IR[6] < 300):
        left_detectBack += 1
    elif(rightAfterBlock == True and sensor.IR[6] < 300):
        right_detectBack += 1

    
    # 뒤가 막히게 된다면
    if(sensor.IR[6] >= 300):
        # 왼쪽으로 가자
        if(leftAfterBlock == True):
            Go(300, 300)
            delay(left_detectBack - 50)
            # 여기서 이제 왼쪽으로 턴하도록 명령 (함수로 만들자)
        if(rightAfterBlock == True):
            Go(300, 300)
            delay(right_detectBack - 50)
            # 여기서 이제 오른쪽으로 턴하도록 명령 (함수로 만들자)

            



Close()