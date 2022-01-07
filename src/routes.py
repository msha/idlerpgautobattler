"""Module containing all routes of the server"""
from os import getenv, urandom
from secrets import token_hex

from flask import abort, jsonify, redirect, render_template, request, session
from flask_login import LoginManager
from werkzeug.security import check_password_hash, generate_password_hash

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
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    print(request.__dict__)
    data = {"name": ":DD"}
    return jsonify(data)


login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login_form"
login_manager.login_message = "Please login to the service"


@login_manager.user_loader
def load_user(user_id):
    return Accounts.query.get(user_id)


db.create_all()
