import pygame
from AltinoLite import *

# 음성 파일 재생
def Al_sound(soundFileName):
    pygame.mixer.init()
    pygame.mixer.music.load("D:\\J.JiYoun\\mp3\\" + soundFileName)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# 알티노 시작 음성
Al_sound("start.mp3")

Open()
Al_sound("conn.mp3")

while 1:
    Go(300, 300)
    Al_sound("go.mp3")
    delay(3000)
    Go(0, 0)
    Al_sound("stopQue.mp3")
    commend = int(input("1 : 출발 / 2 : 이제 그만"))
    print(sensor.CDS)
    if(commend == 1):
        continue
    else:
        break



Close()