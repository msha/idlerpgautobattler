from db import db

class Character(db.Model):

    __tablename = 'character'
    character_id = db.Column(db.Integer, primary_key=True)
    character_owner = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    character_name = db.Column(db.String(144))
    character_level = db.Column(db.Integer)

    def __init__(self) -> None:
        self.character_level = 0

    def set_name(self,name) -> None:
        self.character_name = name

    def get_name(self) -> str:
        return self.character_name

    def get_level(self) -> int:
        return self.character_level