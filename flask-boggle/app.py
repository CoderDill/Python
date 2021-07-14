from flask import Flask, request, render_template, redirect, flash, make_response, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "cool"
app.config['TESTING'] = True
# app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


boggle_game = Boggle()


@app.route("/", methods=['GET', 'POST'])
def boggle_home():
    board = boggle_game.make_board()
    session["board"] = board

    return render_template("boggle_home.html", board=board)


@app.route("/check-guess")
def check_guess(guess):

    board = session["board"]
    res = boggle_game.check_valid_word(board, guess)
    return jsonify({"result": res})
