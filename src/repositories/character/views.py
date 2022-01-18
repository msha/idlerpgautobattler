import functools
import json

from app import app, cron, socketio
from db import db
from flask import abort, jsonify, redirect, render_template, request, session
from flask_login import current_user
from flask_socketio import disconnect, send
from repositories.character.models import Character


def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)

    return wrapped


@app.route("/level_up/<character_id>", methods=["POST"])
def level_up():
    req = request.get_json()
    print(req)
    return "yep", 200


@app.route("/create_dude", methods=["POST"])
def create_character():
    name = request.get_json()["name"]
    new_dude = Character(current_user.id, name)
    db.session.add(new_dude)
    db.session.commit()
    return render_template("index.html")


@app.route("/get_dudes", methods=["GET"])
def get_characters():
    sql = Character.query.filter(Character.character_owner == current_user.id).all()
    data = {}
    data_to_json = []
    for row in sql:
        data = json.loads(row.to_json())
        data_to_json.append(data)
    return json.dumps(data_to_json)


@socketio.on("message")
@authenticated_only
def handleMessage(msg):
    socketio.sleep(0.05)
    send(get_characters(), broadcast=True)


@app.route("/add", methods=["POST"])
def add():
    data = {"return": request.get_json()["name"]}
    return jsonify(data)
