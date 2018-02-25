import socket
import datetime
import os.path

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
    if(os.path.exists(directory)):
        log = open(directory+"/log.txt", "r")
        if log.mode == 'r':
            content =log.read()
            log.close()
        else:
            log.close()
    return content

def getlog():
    writelog()
    data=readlog()
    return data

print(getlog())
