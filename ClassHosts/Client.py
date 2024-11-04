import asyncio
import websockets
import re
from ControllerClass.ClassLinux import RaspBerryPI

class Client:
    # Requisição do BACK-END
    @classmethod
    async def client(self, SERVIDOR, PORT):
        async with websockets.connect(await self._Cliente_realTimeRequest(SERVIDOR, PORT)) as websocket:
            try:
                name = await websocket.send(RaspBerryPI.hostname())
                greeting = await websocket.recv()
                print(f"Client received: {greeting}")
            except websockets.ConnectionClosed:
                print('\033[91m Não possível conectar ao Servidor \033[0m')

    @classmethod
    async def _Cliente_realTimeRequest(self, SERVIDOR, PORT):
        DOMAIN = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w[a-z]+\d{2}\.\w+|\w+\.\w+.com.\w+|\d{1,4}", SERVIDOR).group(0)
        return f'ws://{DOMAIN}:{PORT}'
        
        