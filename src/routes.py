"""Module containing all routes of the server"""
from app import app
from flask import redirect, render_template, request, session, abort
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv
from secrets import token_hex
from db import db
from repositories.user_repository import UserRepository

app.secret_key = getenv("SECRET")
user_repository = UserRepository(db)

def update_session(username, route="/"):
        session["user_id"] = user_repository.find_user_id(username)
        session["username"] = username
        session["csrf_token"] = token_hex(16)
        return redirect(route)

@app.route("/health")
def health():
    return "Health check: ✅"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/log", methods=["POST"])
def log():
    username = request.form["username"]
    password = request.form["password"]
    hash_value = user_repository.find_password(username)
    if hash_value is not None:
        if check_password_hash(hash_value[0], password):
            return update_session(username)
    return render_template("login.html",
                            error="Username and password not matching")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register_account():
    return render_template("create_account.html")

@app.route("/logout")
def logout():
    try:
        del session["user_id"]
        del session["username"]
        del session["csrf_token"]
    except KeyError:
        pass
    return redirect("/")

@app.route("/create_account", methods=["POST"])
def create_account():
    username = request.form["username"]
    password = request.form["password"]
    password_confirm = request.form["passwordConfirm"]

    user_id = user_repository.find_user_id(username)
    if user_id is not None:
        return render_template("create.html", error="Username taken",
                                user=username)
    if password != password_confirm:
        return render_template("create.html",
                                error="Passwords not identical",
                                user=username)

    password = generate_password_hash(password_confirm)
    user_repository.insert_user(username, password)
    return update_session(username)