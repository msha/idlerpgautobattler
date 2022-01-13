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

    def get_id(self):
        return self.id

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def is_authenticated(self):
        return True
