from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
import routes

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login_form"
login_manager.login_message = "Please login to the service"


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)
