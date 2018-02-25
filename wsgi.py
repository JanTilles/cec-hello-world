import socket
import datetime
import os.path
from flask import Flask

application = Flask(__name__)

directory="mnt"

def writelog():
    host= socket.gethostname()
    ts= datetime.datetime.now()
    #if(os.path.exists(directory)):
    log = open(directory+"/log.txt", "a+")
    log.write( host+" "+str(ts)+"\n")
    log.close()
    return

def readlog():
    log = open(directory+"/log.txt", "r")
    content =log.read()
    log.close()
    return content

def getlog():
    writelog()
    data=readlog()
    return data

#application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname()+"\n"

@application.route("/log")
def host():
    return getlog()+"\n"
    
if __name__ == "__main__":
    application.run()
