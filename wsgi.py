import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname()+"\n"

@application.route("/log")
def host():
    print "Test"

host()
    
if __name__ == "__main__":
    application.run()
