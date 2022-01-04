from app import app
from db import db
from repositories.user.user_repository import UserRepository
from flask import redirect, render_template, request, session, abort
from werkzeug.security import check_password_hash, generate_password_hash
from secrets import token_hex

user_repository = UserRepository(db)

def update_session(username, route="/"):
        session["user_id"] = user_repository.find_user_id(username)
        session["username"] = username
        session["csrf_token"] = token_hex(16)
        return redirect(route)

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