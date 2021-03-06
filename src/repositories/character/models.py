import json

import jsonpickle
from db import db


class Character(db.Model):

    __tablename__ = "character"
    
    character_id = db.Column(db.Integer, primary_key=True)
    character_owner = db.Column(
        db.Integer, db.ForeignKey("accounts.id"), nullable=False
    )
    character_name = db.Column(db.String(144))
    character_level = db.Column(db.Integer)

    def __init__(self, owner: int, name: str) -> None:
        self.character_owner = owner
        self.character_name = name
        self.character_level = 0

    def set_name(self, name) -> None:
        self.character_name = name

    def get_name(self) -> str:
        return self.character_name

    def get_level(self) -> int:
        return self.character_level

    def to_json(self):
        data = json.loads(jsonpickle.encode(self))
        data.pop("_sa_instance_state")
        data = jsonpickle.encode(data)
        return data
