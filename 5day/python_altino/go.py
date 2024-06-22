from AltinoLite import *

Open()

IRSet()

back = False
left = False
right = False

Steering(0)

Go(300, 300)

while 1:

    if(left != False or right != False):
        Steering(0)

    print(sensor.IR[1], sensor.IR[2],sensor.IR[3], sensor.IR[6])

    if(sensor.IR[1] > 10):
        right = True
        Steering(10)
    else:
        right = False

    if(sensor.IR[3] > 10):
        left = True
        Steering(-10)
    else:
        left = False

    if(sensor.IR[2] > 20 and back == False):
        back = True
        Go(0, 0)
        Light(0x05)
        delay(1000)
        Light(0x00)
        Go(-300, -300)
    elif(sensor.IR[6]>30):
        back = False
        # Go(0, 0)
        # Light(0x05)
        # delay(1000)
        # Light(0x00)
        Go(300, 300)

Go(0, 0)    

Close()