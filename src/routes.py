"""Module containing all routes of the server"""
from app import app
from flask import redirect, render_template, request, session, abort
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv
from secrets import token_hex
from db import db

app.secret_key = getenv("SECRET")