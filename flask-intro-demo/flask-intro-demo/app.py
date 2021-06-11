from logging import debug
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)

app.config["SECRET_KEY"] = 'coolbeans'
debug = DebugToolbarExtension(app)

COMPLIMENTS = ['cool', 'clever', 'Pythonic', 'awesome']


@app.route('/spell/<word>')
def get_spell(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)


@app.route('/')
def home_page():
    """Shows home page"""
    return render_template('home.html')


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/form_2')
def show_form_2():
    return render_template('form_2.html')


@app.route('/greet')
def get_greeting():
    username = request.args["username"]
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)


@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet-2.html', username=username, wants_compliments=wants, compliments=nice_things)


@app.route('/lucky')
def lucky_num():
    num = randint(1, 5)
    return render_template('lucky.html', lucky_num=num, msg="You are so lucky!")
