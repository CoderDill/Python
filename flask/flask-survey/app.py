from flask import Flask, request, render_template, redirect, flash, make_response, session
from flask_debugtoolbar import DebugToolbarExtension
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

    survey = surveys[survey_id]
    session[CURRENT_SURVEY_KEY] = survey_id

    return render_template("start_survey.html", survey=survey)


@app.route("/start", methods=["POST"])
def start_survey():
    session[RESPONSES_KEY] = []

    return redirect("questions/0")


@app.route("/answer", methods=["POST"])
def handle_questions():
    answer = request.form["answer"]
    text = request.form.get("text", "")

    responses = session[RESPONSES_KEY]
    responses.append({"answer": answer, "text": text})

    session[RESPONSES_KEY] = responses
    survey_code = session[CURRENT_SURVEY_KEY]
    survey = surveys[survey_code]

    if (len(responses) == len(survey.questions)):
        return redirect("/completed")
    else:
        return redirect(f"/questions/{len(responses)}")


@app.route("/questions/<int:question_id>")
def show_question(question_id):
    """Display current question."""
    responses = session.get(RESPONSES_KEY)
    survey_code = session[CURRENT_SURVEY_KEY]
    survey = surveys[survey_code]

    if (responses is None):
        return redirect("/")

    if (len(responses) == len(survey.questions)):
        return redirect("/completed")

    if (len(responses) != question_id):
        flash(f"Invalid question: {question_id}")
        return redirect(f"/questions/{len(responses)}")

    question = survey.questions[question_id]

    return render_template(
        "question.html", question=question)


@app.route("/completed")
def thank_you():
    survey_id = session[CURRENT_SURVEY_KEY]
    survey = surveys[survey_id]
    responses = session[RESPONSES_KEY]

    html = render_template("completed.html",
                           survey=survey,
                           responses=responses)

    response = make_response(html)
    response.set_cookie(f"completed_{survey_id}", "yes")
    return response
