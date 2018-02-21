import socket
import datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    
    return datetime.date.today()+" "+socket.gethostname()+"\n"


if __name__ == "__main__":
    application.run()
