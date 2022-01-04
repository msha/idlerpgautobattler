from app import db

class Character(db.Model):

    character_id = db.Column(db.Integer, primary_key=True)

    def __init__(self) -> None:
        super().__init__()