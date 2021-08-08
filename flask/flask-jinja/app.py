from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = 'coolbeans'
debug = DebugToolbarExtension(app)

@app.route("/")
def home_page():
    
    return render_template("home.html")
