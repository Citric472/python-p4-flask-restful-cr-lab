from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __init__(self, name, image, price):
        self.name = name
        self.image = image
        self.price = price

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': self.price
        }
