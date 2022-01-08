from app import app
from db import db
from flask import abort, jsonify, redirect, render_template, request, session
from repositories.character.models import Character


@app.route("/level_up")
def level_up():
    return render_template("index.html")


@app.route("/create_dude", methods=["POST"])
def create_character():
    name = request.get_json()["name"]
    new_dude = Character(session["user_id"], name)
    db.session.add(new_dude)
    db.session.commit()
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    data = {"return": request.get_json()["name"]}
    return jsonify(data)
