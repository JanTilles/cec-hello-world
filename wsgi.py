import socket
import datetime
import os.path
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname()+"\n"

@application.route("/log")
def host():
    directory="/mnt/"

    def writelog():
        host= socket.gethostname()
        ts= datetime.datetime.now()       
        log = open(os.path.join(directory,"log.txt"), "a+")
        #log = open("log.txt", "a+")
        log.write("Hostname:"+host+" Timestamp:"+str(ts)+'\n')
        log.close()
        return

    def readlog():     
        log = open(os.path.join(directory,"log.txt"), "r")
        #log = open("log.txt", "r")
        content =log.read()
        log.close()
        return content

    def getlog():
        writelog()
        data=readlog()
        return data
    
    return getlog()+"\n"
    
if __name__ == "__main__":
    application.run()
