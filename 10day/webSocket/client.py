import asyncio
# pip install websockets
import websockets
# pip install aioconsole
import aioconsole


# 요청하고 받을 서버 주소
async def send_and_receive():
    uri = "ws://home.sjkim.net:8888" # url = http://naver.com \\ uri = http://naver.com/?id=23
    async with websockets.connect(uri) as websocket:
        send_task = asyncio.create_task(send(websocket))
        receive_task = asyncio.create_task(receive(websocket))
        await asyncio.gather(send_task, receive_task)




# 보낼거
async def send(websocket):

    while 1: # 한 번 끝나면 다시 실행
        # 무전기에 말할 내용
        # message = input("채팅창 : ") # input은 동기방식 즉, 비동기 안에 동기가 있으면 안됨
        message = await aioconsole.ainput(" 채팅창 : ")

        # 무전기에 말하자
        await websocket.send(message) # "다 했어요!" 완료라고 말해줌


# 받을거
async def receive(websocket):
    async for message in websocket :
        print("다른사람 말 : "+message)


asyncio.get_event_loop().run_until_complete(send_and_receive()) # send_and_receive() 가 모두 실행될 때까지 계속 실행