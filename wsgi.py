import socket;
import datetime;
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    return socket.gethostname()+"\n"

@application.route("/log")
def host():
    return socket.gethostname()+"\n"

def time():
    return datetime.date()+"\n"

if __name__ == "__main__":
    application.run()
