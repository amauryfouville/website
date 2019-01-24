#Import dependencies
from flask import Flask, render_template

#Create instance of Flask App
app = Flask(__name__)

#Define Route and content of that page
@app.route("/")
def home():
    return render_template("index.html")

#Define 2nd route and content
@app.route("/formation")
def about():
    return render_template("formation.html")

@app.route("/atouts")
def atouts():
    return render_template("atouts.html")

#Running and Controlling the script
if (__name__ =="__main__"):
	app.run(port=80, host=0.0.0.0, debug=True)