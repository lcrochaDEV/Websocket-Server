import asyncio
import websockets


SERVIDOR = "ws://192.168.1.254:8765"
LOCALHOST = 'ws://localhost:8765'

async def hello():
    async with websockets.connect(SERVIDOR) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f'Client sent: {name}')

        greeting = await websocket.recv()
        print(f"Client received: {greeting}")

asyncio.get_event_loop().run_until_complete(hello())