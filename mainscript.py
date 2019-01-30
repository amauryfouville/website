from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import locations

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

#Définitioin des routes et des contenus des pages

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

@app.route("/map")
def map():
	
    return render_template("maps.html")

@app.route("/add")


#Running and Controlling the script
if (__name__ =="__main__"):
	app.run(port=80, host='0.0.0.0', debug=True)