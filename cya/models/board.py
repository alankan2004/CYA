from db import db

class BoardModel(db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    cards = db.relationship('CardModel')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name' : self.name, 'cards': [card.json() for card in self.cards]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()