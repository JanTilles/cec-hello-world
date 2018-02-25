import socket
import io_library
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname()+"\n"

@application.route("/log")
def host():
    return io_library.getlog()+"\n"
    
if __name__ == "__main__":
    application.run()
