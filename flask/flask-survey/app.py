from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.wrappers import response
from surveys import surveys

# key names will use to store some things in the session;
# put here as constants so we're guaranteed to be consistent in
# our spelling of these
CURRENT_SURVEY_KEY = 'current_survey'
RESPONSES_KEY = 'responses'

app = Flask(__name__)
app.config['SECRET_KEY'] = "cool"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


@app.route("/")
def survey_home():
    return render_template("survey_home.html", surveys=surveys)


@app.route("/", methods=["POST"])
def pick_survey():
    survey_id = request.form["survey_code"]

    if request.cookies.get(f"completed_{survey_id}"):
        return render_template("survey_done.html")

    survey = surveys[survey_id]
    session[CURRENT_SURVEY_KEY] = survey_id

    return render_template("start_survey.html", survey=survey)


@app.route("/start", methods=["POST"])
def start_survey():
    session[RESPONSES_KEY] = []

    return redirect("questions/0")


@app.route("/questions/0")
def questions():
    res = session.get(RESPONSES_KEY)
    survey_code = session[CURRENT_SURVEY_KEY]
    survey = surveys[survey_code]

    question = survey.questions[0]
    return render_template("/question.html", question=question)
