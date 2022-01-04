"""Module containing all routes of the server"""
from app import app
from flask import redirect, render_template, request, session, abort
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv
from secrets import token_hex
from db import db

from repositories.user.user_repository import UserRepository
from repositories.user import views

from repositories.character import views

from os import urandom

app.secret_key = urandom(32)

user_repository = UserRepository(db)


@app.route("/")
def index():
    return render_template("index.html")


db.create_all()
