from dotenv import load_dotenv
import os
from Async.ClassAsync import AssyncExec
from ClassHosts.Server import Server

load_dotenv()

SERVER = os.getenv("SERVER")
SERVER_PORT = os.getenv("SERVER_PORT")
CLIENT_PORT = os.getenv("CLIENT_PORT")

AssyncExec.asyncAction(
    Server.realTimeRequest(SERVER, SERVER_PORT),
    #Server.commandDebug(SERVER, CLIENT_PORT),
)
