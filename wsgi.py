import socket
import time
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname()+"\n"

@application.route("/log/")
def log():
    host = socket.gethostname()
    timestamp = time.time()
        
        return host, timestamp"\n"

if __name__ == "__main__":
    application.run()
