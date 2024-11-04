from dotenv import load_dotenv
import os
from Async.ClassAsync import AssyncExec
from ClassHosts.Server import Server
from ClassHosts.ClienteDebug import ClienteDebug
load_dotenv()

SERVER = os.getenv("SERVER")
SERVER_PORT = os.getenv("SERVER_PORT")
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
    ClienteDebug.ClienteDebug_realTimeRequest(SERVER, CLIENT_DEBUG),
)
