from flask import Flask, request, render_template
import ranint
from 
app = Flask(__name__)


@app.route("/lucky")
def lucky_number():
    num = ranint(1, 1000)
    return render_template("lucky.html", lucky_num=num)
