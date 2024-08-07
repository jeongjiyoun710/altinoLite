import asyncio
# pip install websockets
import websockets

# 무전기 저장소
clients = set()

# 객체 클래스
class Client:
    def __init__(self, name, web_key):
        self.name = name
        self.web_key = web_key
        

async def myServer(websocket, path):


    # clients.add(websocket)

    try:
        async for name in websocket:
            print("새로운 사람의 이름 : "+name)

            # 객체로 client 만든 후, 그 객체를 추가
            client = Client(name, websocket)
            clients.add(client)

            # 확인
            for i in clients:
                if(i.name == name):
                    print("이름 : "+i.name+"key : "+str(i.web_key))

            print("접속자수 : " + str(len(clients)))
            await websocket.send("환영합니다!"+name+"님!")

    except:
        print("이름 실패")



    try:
        async for message in websocket:
            print("client message : " + message)
            for clientSockets in clients:
                await clientSockets.send(message)
    except websockets.ConnectionClosed:
        clients.remove(websocket)
        print("1명이 나갔습니다. 현재 접속자수 : " + str(len(clients)))


start_server = websockets.serve(myServer, "localhost", 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever() #서버는 꺼질 일 없잖아?