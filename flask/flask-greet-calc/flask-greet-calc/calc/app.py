from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_it():
    a = int(request.args["a"])
    b = int(request.args["b"])
    total = add(a, b)
    return str(total)


@app.route("/sub")
def sub_it():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a - b)


@app.route("/mult")
def mult_it():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a * b)


@app.route("/div")
def div_it():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a / b)
