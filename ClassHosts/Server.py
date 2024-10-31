import asyncio
import websockets
from subprocess import check_output 

class Server:

    # Requisição do FRONT-END    
    @classmethod
    async def realTimeRequest(self, SERVIDOR, PORT):
        await self._main(self._report, SERVIDOR, PORT)

    @classmethod
    async def _report(self, websocket):
        reply = await websocket.recv()
        command = check_output(reply)
        await websocket.send(command)

    # Command Console
    @classmethod
    async def commandDebug(self, SERVIDOR, PORT):
        await self._main(self._server, SERVIDOR, PORT)
         
    @classmethod
    async def _server(self, websocket):
        await self._connect_client_ip(websocket)
        
        name = await websocket.recv() # RECEBE DO CLIENTE
        
        print(f'Server Received: {name}') 
        greeting = f'Hello {name}!'

        await websocket.send(greeting) # ENVIA PARA O CLIENTE
        print(f'Server Sent: {greeting}')

    @classmethod
    async def _connect_client_ip(self, websocket):
        IP_CLIENTE = websocket.remote_address
        print(f'Host IP: {IP_CLIENTE[0]} Conectado.')

    @classmethod
    async def _main(self, SERVER, SERVIDOR, PORT):
        async with websockets.serve(SERVER, SERVIDOR, PORT):
            await asyncio.Future()  # run forever
