import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return socket.gethostname(),time.strftime("%X")+"\n"


if __name__ == "__main__":
    application.run()
