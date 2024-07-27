import asyncio
# pip install websockets
import websockets

# 무전기 저장소
clients = set()
async def myServer(websocket, path):


    clients.add(websocket)
    print("접속자수 : " + str(len(clients)))

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