import asyncio
import websockets

SERVIDOR = "ws://192.168.1.254:8732"
LOCALHOST = 'ws://localhost:8765'

async def client():
    async with websockets.connect(SERVIDOR) as websocket:
        try:
            name = input("Digite um Comando: ")

            await websocket.send(name)
            print(f'Client sent: {name}')

            greeting = await websocket.recv()
            print(f"Client received: {greeting}")
        except websockets.ConnectionClosed:
            print('\033[91m Não possível conectar ao Servidor \033[0m')

asyncio.get_event_loop().run_until_complete(client())
