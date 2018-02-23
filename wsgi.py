import socket
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname()+"\n"

@application.route("/log")
def log():
    return socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
