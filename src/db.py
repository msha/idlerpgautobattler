"""Handles transactions with the database"""
from os import getenv

from flask_sqlalchemy import SQLAlchemy

from app import app

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
