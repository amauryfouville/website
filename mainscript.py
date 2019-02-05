import os
import ast
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from models import location, db

"""def create_app():
    app = Flask(__name__)
    db.init_app(app)
    return app"""

#Create instance of Flask App
app = Flask(__name__)

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
app.app_context().push()

"""
allLocations=location.query.all()

print("1")
print(json.dumps([loc.serialize() for loc in allLocations]))
print(type(json.dumps([loc.serialize() for loc in allLocations])))


print("2")
print(jsonify(local=[l.serialize() for l in allLocations]))


print("3")
variable = json.loads(json.dumps([loc.serialize() for loc in allLocations]))

print(variable[0])
print(variable[0].get("id"))

print(json.loads(json.dumps([loc.serialize() for loc in allLocations])))
print(type(json.loads(json.dumps([loc.serialize() for loc in allLocations]))))
"""


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


@app.route("/test")
def test():
	allLocations=location.query.all()
	#return(json.dumps([loc.serialize() for loc in allLocations]))


	return render_template("test.html", data=json.loads(json.dumps([loc.serialize() for loc in allLocations])))

@app.route("/map",methods=['GET', 'POST'])
def map():
	allLocations=location.query.all()
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
			allLocations=location.query.all()
			return render_template("maps.html",data=json.loads(json.dumps([loc.serialize() for loc in allLocations])))
		except Exception as e:
			return(str(e))
	return render_template('maps.html', data=json.loads(json.dumps([loc.serialize() for loc in allLocations])))

if (__name__ =="__main__"):
	app.run(port=80, host='0.0.0.0', debug=True)