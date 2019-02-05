from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60),nullable=False)
    lat = db.Column(db.Float(), nullable=False)
    long = db.Column(db.Float(), nullable =False)
    type = db.Column(db.String(15), nullable=False)
    

    def __init__(self, name, lat, long, type):
        self.name = name
        self.lat = lat
        self.long = long
        self.type = type

    def __repr__(self):
        return '<Name %r>' % self.name
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'lat': self.lat,
            'long': self.long,
            'type': self.type
            } 

