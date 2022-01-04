from db import db


class Accounts(db.Model):

    __tablename = "accounts"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    def __init__(self, id, username, password) -> None:
        self.id = id
        self.username = username
        self.password = password
