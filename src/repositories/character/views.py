import json

from app import app, socketio
from db import db
from flask import abort, jsonify, redirect, render_template, request, session
from flask_socketio import send
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


@app.route("/get_dudes", methods=["GET"])
def get_characters():
    sql = Character.query.filter(Character.character_owner == session["user_id"]).all()
    data = {}
    d = []
    for row in sql:
        data = json.loads(row.to_json())
        d.append(data)
    return json.dumps(d)


@socketio.on("message")
def handleMessage(msg):
    send(get_characters(), broadcast=True)


@app.route("/add", methods=["POST"])
def add():
    data = {"return": request.get_json()["name"]}
    return jsonify(data)
