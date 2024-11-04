from dotenv import load_dotenv
import os
from Async.ClassAsync import AssyncExec
from ClassHosts.Server import Server
from ClassHosts.Client import Client
from ClassHosts.ClientDebug import ClientDebug
load_dotenv()

SERVER = os.getenv("SERVER")
SERVER_PORT = os.getenv("SERVER_PORT")
CLIENT = os.getenv("CLIENT")
CLIENT_DEBUG = os.getenv("CLIENT_DEBUG")

'''
#START SERVER
AssyncExec.asyncAction(
    Server.realTimeRequest(SERVER, SERVER_PORT),
    Server.commandDebug(SERVER, CLIENT_DEBUG),
)
'''
#START CLIENT
AssyncExec.asyncAction(
    ClientDebug.client(CLIENT, SERVER_PORT),
)

'''
#START CLIENT
AssyncExec.asyncAction(
   ClientDebug.debug(SERVER, CLIENT_DEBUG),
)
'''
