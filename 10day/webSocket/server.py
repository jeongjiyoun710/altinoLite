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
        async for message in websocket:

            name_check = False #이름 없음

            # 현재 메세지를 보낸 웹소켓이 배열에 저장되어 있는지 확인
            for i in clients:
                # print(i.name + " : 현재 이름")
                if(i.web_key == websocket):
                    name_check = True
                
            if(name_check == False): # 지금 쓴 것이 이름일 경우를 말함. 
                print("새로운 사람의 이름 : "+message)

                # 객체로 client 만든 후, 그 객체를 추가 (이름, 웹소켓 키)
                client = Client(message, websocket)
                clients.add(client)

                # 객체 추가 됐는지 확인
                # for i in clients:
                #     if(i.name == message):
                #         print("이름 : "+i.name+"key : "+str(i.web_key))


                print("접속자수 : " + str(len(clients)))
                await websocket.send("환영합니다!"+message+"님!")

            else: # 이미 이름이 존재하는 사람임. 즉 지금 쓴거는 이름이 아니라 메세지라는 것!

                class nameAndMessage:
                    def __init__(self, name, message):
                        self.name = name
                        self.message = message

                name = ""

                for i in clients:
                    if(i.web_key == websocket):
                        name = i.name

                if(name != ""):
                    print(name + " : " + message)
                    for clientSockets in clients:
                        # 지금 메세지를 보낸 웹소켓이랑 객체의 웹소켓 키가 같지 않을 경우에만 보냄
                        if(clientSockets.web_key != websocket):
                            # 객체로 전송 => 객체로 보내니 client에서 받을 때 오류가 걸림..
                            # await clientSockets.web_key.send(nameAndMessage(name, message))
                            # print()
                            await clientSockets.web_key.send(message)

                
                else:
                    print("client message : " + message)
                    for clientSockets in clients:
                        # 객체로 전송
                        # await clientSockets.web_key.send(nameAndMessage("client", message))
                        await clientSockets.web_key.send(message)

    except:
        clients.remove(websocket)
        print("1명이 나갔습니다. 현재 접속자수 : " + str(len(clients)))



    # try:
    #     async for message in websocket:

    #         name = ""

    #         for i in clients:
    #             if(i.web_key == websocket):
    #                 name = i.name

#             print("client message : " + message)
#             for clientSockets in clients:
#                 await clientSockets.send(message)


    # except websockets.ConnectionClosed:
    #     clients.remove(websocket)
    #     print("1명이 나갔습니다. 현재 접속자수 : " + str(len(clients)))


start_server = websockets.serve(myServer, "localhost", 8888)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever() #서버는 꺼질 일 없잖아?