from AltinoLite import *

Open() #명령 시작 ≒ file.open("...", r)
print("알티노라이트 시작")


while 1:
    print(sensor.CDS)
    if(sensor.CDS < 20):
        Light(0x03)
    else:
        Light(0x00)


Close() #명령 끝, 닫기 ≒ file.close()