import socket
import datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
	return socket.gethostname()+"\n"

@application.route("/log/")
def log():
    host = socket.gethostname()
	timestamp = datetime.datetime.now()
	
	return host, timestamp"\n"

if __name__ == "__main__":
    application.run()
