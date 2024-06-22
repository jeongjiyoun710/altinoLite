from AltinoLite import *

Open()

# 적외선 센서 초기화
#IRSet()

Go(300, 300)

altino = 'F'

while 1 : 
    if(sensor.IR[2] > 5):
        if ( altino == 'F') :
            Go(-300,-300)
            altino ='B'

    elif (sensor.IR[6] > 30) :
        if ( altino == 'B') :
            Go(300,300)
            altino ='F'
        


Close()