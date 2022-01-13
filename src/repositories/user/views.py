from app import app
from db import db
from flask import abort, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user
from flask_socketio import disconnect
from repositories.user.models import Accounts
from repositories.user.user_repository import UserRepository
from werkzeug.security import check_password_hash, generate_password_hash

user_repository = UserRepository(db)


@app.route("/log", methods=["POST"])
def log():
    post_username = request.form["username"].strip()
    post_password = request.form["password"].strip()

    user = Accounts.query.filter_by(username=post_username).first()
    hash_value = user_repository.find_password(post_username)
    if not user:
        return render_template("login.html", error="user not found")
    if hash_value is not None:
        if check_password_hash(hash_value[0], post_password):
            login_user(user, remember=True)
            print("login successful")
            return render_template("index.html")
    return render_template("login.html", error="Username and password not matching")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/create_account", methods=["POST"])
def create_account():
    post_username = request.form["username"].strip()
    post_password = request.form["password"].strip()
    post_password_confirm = request.form["passwordConfirm"].strip()

    user_id = user_repository.find_user_id(post_username)
    if user_id is not None:
        return render_template(
            "create.html", error="Username taken", user=post_username
        )
    if post_password != post_password_confirm:
        return render_template(
            "create.html", error="Passwords not identical", user=post_username
        )

    post_password = generate_password_hash(post_password_confirm)
    user_repository.insert_user(post_username, post_password)
    user = Accounts.query.filter_by(username=post_username).first()
    login_user(user)
    return render_template("index.html")


@app.route("/register")
def register_account():
    return render_template("create_account.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")
