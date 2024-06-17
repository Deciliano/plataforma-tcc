from datetime import datetime
from db import db

class Product(db.Model):
        __tablename__ = 'products'

        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(80), nullable=False)
        desc = db.Column(db.String(200), nullable=True)
        price = db.Column(db.Float, nullable=False)
        quantity = db.Column(db.Integer, nullable=False)
        created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
        updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)

        def to_dict(self):
                return {
                'id': self.id,
                'name': self.name,
                'desc': self.desc,
                'price': self.price,
                'quantity': self.quantity,
                'created_at': self.created_at,
                'updated_at': self.updated_at
                }