import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8080"  
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        print("Message sent to server.")
        response = await websocket.recv()
        print(f"Message from server: {response}")

asyncio.get_event_loop().run_until_complete(hello())
