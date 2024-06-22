from AltinoLite import *

Open()

IRSet()
while 1:
    print("전방좌측 : " + str(sensor.IR[1]) + " | 전방가운데 : " + str(sensor.IR[2]) + " | 전방우측 : " + str(sensor.IR[3]) + " | 오른쪽 : " + str(sensor.IR[4]) + " | 왼쪽 : " + str(sensor.IR[5]) + " | 후방 : " + str(sensor.IR[6]))

Close()