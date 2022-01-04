from app import app
from db import db
from repositories.character.models import Character
from flask import redirect, render_template, request, session, abort


@app.route("/level_up")
def level_up():
    db.session.query(Character)
    return render_template("index.html")
