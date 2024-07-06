import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from AltinoLite import *
from PyQt5.QtCore import QThread, pyqtSignal
import time

form_class = uic.loadUiType("D:\\J.JiYoun\\python_class\\7day\\altino.Ui")[0]

# 회전값
rotate = 0

# 연결확인
connectFlag = False

# 쓰레드 선언
class Thread1(QThread):
    updateSignal = pyqtSignal(int)
    def run(self):
        while (connectFlag == True):
            # 센서 값을 시그널로 보냅니다
            time.sleep(0.05)
            self.updateSignal.emit("test")


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

class Mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 내가 원하는 기능 추가
        self.btnConnectAltino.clicked.connect(self.fn_connectAltino)
        self.btnDisconnectAltino.clicked.connect(self.fn_disConnectAltion)

        self.altinoGo.clicked.connect(self.fn_go)
        self.altinoBack.clicked.connect(self.fn_back)
        self.altinoStop.clicked.connect(self.fn_stop)
        self.altinoRight.clicked.connect(self.fn_right)
        self.altinoLeft.clicked.connect(self.fn_left)
        self.altinoSteeringNone.clicked.connect(self.fn_sterringNone)

        self.thread = Thread1()
        self.thread.updateSignal.connect(self.updateSensor)
        
    def fn_connectAltino(self):
        Open()

        global connectFlag
        connectFlag = True
        self.thread.start()

        self.txtAltinoStatus.setText("연결완료")
        

    def fn_disConnectAltion(self):
        Close()

        global connectFlag
        connectFlag = False
        self.txtAltinoStatus.setText("미연결")

    def fn_go(self):
        Go(300, 300)

    def fn_back(self):
        Go(-300, -300)

    def fn_stop(self):
        Go(0, 0)
        Sound(30)
        delay(100)
        Sound(0)

    def fn_sterringNone(self):
        global rotate

        rotate=0
        Steering(rotate)

    def fn_right(self):
        global rotate

        rotate += 20
        Steering(rotate)

    def fn_left(self):
        global rotate

        rotate -= 20
        Steering(rotate)

    # 스레드 시그널 도착!
    def updateSensor(self, value):
        print("왔다!")
        self.lightSensor.setText(str(sensor.CDS))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Mywindow()
    myWindow.show()
    app.exec_()