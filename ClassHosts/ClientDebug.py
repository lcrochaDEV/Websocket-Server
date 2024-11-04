import asyncio
import websockets
from ClassHosts.Client import Client

import re
class ClientDebug(Client):
    
    # Requisição do BACK-END
    @classmethod
    async def debug(self, SERVIDOR, PORT):
        async with websockets.connect(await self._Cliente_realTimeRequest(SERVIDOR, PORT)) as websocket:
            try:
                name = input("Digite um Comando: ")

                await websocket.send(name)
                print(f'Client sent: {name}')

                greeting = await websocket.recv()
                print(f"Client received: {greeting}")
            except websockets.ConnectionClosed:
                print('\033[91m Não possível conectar ao Servidor \033[0m')
