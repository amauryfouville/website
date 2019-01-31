from mainscript import db

class location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    lat = db.Column(db.Float())
    long = db.Column(db.FLoat())
    type = db.Column(db.String())
    

    def __init__(self, name, author, published):
        self.name = name
        self.lat = lat
        self.long = long
        self.type = type

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'lat': self.lat,
            'long':self.long,
            'type':self.type
            }