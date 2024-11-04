import asyncio
import websockets
import re


class ClienteDebug:
    # Requisição do BACK-END
    @classmethod
    async def _client(self, DOMAIN):
        async with websockets.connect(DOMAIN) as websocket:
            try:
                name = input("Digite um Comando: ")

                await websocket.send(name)
                print(f'Client sent: {name}')

                greeting = await websocket.recv()
                print(f"Client received: {greeting}")
            except websockets.ConnectionClosed:
                print('\033[91m Não possível conectar ao Servidor \033[0m')

    @classmethod
    async def ClienteDebug_realTimeRequest(self, SERVIDOR, PORT):
        DOMAIN = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\w[a-z]+\d{2}\.\w+|\w+\.\w+.com.\w+|\d{1,4}", SERVIDOR).group(0)
        await self._client(f'ws://{DOMAIN}:{PORT}')
