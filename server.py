import asyncio
import websockets

SERVIDOR = '192.168.1.254'

async def hello(websocket):
    name = await websocket.recv()
    print(f'Server Received: {name}')
    greeting = f'Hello {name}!'

    await websocket.send(greeting)
    print(f'Server Sent: {greeting}')

async def main():
    async with websockets.serve(hello, SERVIDOR, 8765):
        await asyncio.Future()  # run forever

asyncio.get_event_loop().run_until_complete(main())