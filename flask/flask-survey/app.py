from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import surveys

# key names will use to store some things in the session;
# put here as constants so we're guaranteed to be consistent in
# our spelling of these
RESPONSES_KEY = "responses"

app = Flask(__name__)
app.config['SECRET_KEY'] = "cool"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def survey_home():
    return render_template("survey_home.html", surveys=surveys)


@app.route("/", methods=["POST"])
def pick_survey():
    survey_id = request.form[""]
    print(survey_id)
    return render_template("start_survey.html")
