import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
#from models import location


#Create instance of Flask App
app = Flask(__name__)

db = SQLAlchemy()

POSTGRES = {
    'user': 'vwbdbcvjiqxqsd',
    'pw': 'eb5fbd3b9b1367b125c223d7956aa1414038e565bc01f317606b1e30a5c4d38f',
    'db': 'dc7phhigdmm0d8',
    'host': 'ec2-54-228-224-37.eu-west-1.compute.amazonaws.com',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)

class location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    lat = db.Column(db.Float())
    long = db.Column(db.Float())
    type = db.Column(db.String())
    

    def __init__(self, name, lat, long, type):
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

#Définition des routes et des contenus des pages

#Accueil / Compétences, à séparer
@app.route("/")
def home():
    return render_template("index.html")

#formation
@app.route("/formation")
def formation():
    return render_template("formation.html")

@app.route("/atouts")
def atouts():
    return render_template("atouts.html")

@app.route("/map",methods=['GET', 'POST'])
def map():
	if request.method == 'POST':
		name=request.form.get('name')
		lat=request.form.get('lat')
		long=request.form.get('long')
		try:
			loc=location(
				name=name,
				lat=lat,
				long=long,
				type='suggestion'
			)
			db.session.add(loc)
			db.session.commit()
			return "Ville ajoutée. id={}".format(loc.id)
		except Exception as e:
			return(str(e))
	return render_template("maps.html")

if (__name__ =="__main__"):
	app.run(port=80, host='0.0.0.0', debug=True)