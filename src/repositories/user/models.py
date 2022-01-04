from db import db


class Accounts(db.Model):

    __tablename = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
