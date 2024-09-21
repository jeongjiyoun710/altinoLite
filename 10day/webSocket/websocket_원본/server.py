import asyncio
import websockets

clients = set()

async def echo(websocket, path):
    clients.add(websocket)
    try:
        async for message in websocket:

            print("clientMessage: " + message)
            await broadcast(message, websocket)

    except websockets.ConnectionClosed:
        print("Connection closed")
    finally:
        clients.remove(websocket)




async def broadcast(message, sender):
    for client in clients:
        await client.send(message)

start_server = websockets.serve(echo, "0.0.0.0", 8080)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
