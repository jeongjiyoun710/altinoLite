from datetime import datetime
import time
import random

now = 0

while now < 5:

    # 변수 생성
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    # 정답
    gugudan = a * b

    print("구구단을 외자 !")
    print(a,"*",b,"= ?")

    # 타이머 스타트 (현재의 시간이 나옴)
    start_time = datetime.now()

    # 답 입력
    user = float(input("답 >>"))

    end_time = datetime.now()

    timer = start_time - end_time

    time_out = int(timer.total_seconds())


    # 시간 확인 (5초 지나면 아웃)
    if(time_out <= -5) :
        print('시간 초과!')
        now += 10
    else : 
        # 확인
        if(user == gugudan) :
            print("정답입니다!")
            now+=1
        else :
            print("이걸 틀리냐 ㅋ")
            now+=10



        

now = 0