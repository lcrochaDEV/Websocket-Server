import asyncio
import websockets
from ControllerClass.ClassLinux import *
from Async.ClassAsync import AssyncExec

SERVIDOR = '192.168.1.254'

async def server(websocket):
    
    connect_client_ip(websocket)

    name = await websocket.recv() # RECEBE DO CLIENTE
    
    print(f'Server Received: {name}') 
    greeting = f'Hello {name}!'

    await websocket.send(greeting) # ENVIA PARA O CLIENTE
    print(f'Server Sent: {greeting}')

async def main():
    async with websockets.serve(server, SERVIDOR, 8761):
        await asyncio.Future()  # run forever


def connect_client_ip(websocket):
    IP_CLIENTE = websocket.remote_address
    print(f'Host IP: {IP_CLIENTE[0]} Conectado.')

AssyncExec.asyncAction(main(),)

#asyncio.get_event_loop().run_until_complete(main())
