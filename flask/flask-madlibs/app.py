from logging import debug
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import story

app = Flask(__name__)

app.config["SECRET_KEY"] = 'coolbeans'
debug = DebugToolbarExtension(app)


@app.route("/")
def get_home():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route("/story")
def get_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)
