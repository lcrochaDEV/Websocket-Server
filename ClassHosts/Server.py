import asyncio
import websockets
from ControllerClass.ClassLinux import *


SERVIDOR = '192.168.1.254'

class Server:

    @classmethod
    async def server(self, websocket):
        await self.connect_client_ip(websocket)
        
        name = await websocket.recv() # RECEBE DO CLIENTE
        
        print(f'Server Received: {name}') 
        greeting = f'Hello {name}!'

        await websocket.send(greeting) # ENVIA PARA O CLIENTE
        print(f'Server Sent: {greeting}')
    
    @classmethod
    async def connect_client_ip(self, websocket):
        IP_CLIENTE = websocket.remote_address
        print(f'Host IP: {IP_CLIENTE[0]} Conectado.')
        pass

    @classmethod
    async def main(self):
        async with websockets.serve(self.server, SERVIDOR, 8731):
            await asyncio.Future()  # run forever
