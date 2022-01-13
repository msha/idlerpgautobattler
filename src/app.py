from flask import Flask
from flask_apscheduler import APScheduler
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)
cron = APScheduler()

cron.init_app(app)
cron.start()

import routes

if __name__ == "__main__":
    socketio.run(app)
