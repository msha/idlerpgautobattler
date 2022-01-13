"""Module containing all routes of the server"""
from os import getenv, urandom

from flask import abort, jsonify, redirect, render_template, request, session
from flask_login import LoginManager, current_user
from flask_socketio import disconnect

from app import app
from db import db
from repositories.character import views
from repositories.user import models, views
from repositories.user.models import Accounts
from repositories.user.user_repository import UserRepository

app.secret_key = urandom(32)

user_repository = UserRepository(db)


@app.route("/")
def index():
    if not current_user.is_authenticated:
        return render_template("login.html")
    return render_template("index.html")


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = "Please login to the service"


@login_manager.user_loader
def load_user(user_id):
    return Accounts.query.get(user_id)


import functools


def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)

    return wrapped


db.create_all()
