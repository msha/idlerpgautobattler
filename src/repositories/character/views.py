from app import app
from db import db
from repositories.character.models import Character
from flask import redirect, render_template, request, session, abort


@app.route("/level_up")
def level_up():
    return render_template("index.html")


@app.route("/create_dude")
def create_character():
    return render_template("index.html")
