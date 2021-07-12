from flask import Flask, request, render_template, redirect, flash, make_response, session
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle
from axios import "axios"

app = Flask(__name__)
app.config['SECRET_KEY'] = "cool"
app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True

debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route("/")
def boggle_home():
    board = boggle_game.make_board()
    return render_template("boggle_home.html", board=board)

@app.route("/", methods={"POST"})
def enter_guess():

    return render_template()