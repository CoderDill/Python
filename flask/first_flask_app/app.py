from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home_page():
    html = """
    <html>
        <body>
        <h1>Hello!</h1>
        <p>This is the home page.</p>
        <a href="/hello">Hello Page</a>
        </body>
    </html>
    """
    return html

@app.route("/hello")
def say_hello():
    html = """
    <html>
        <body>
        <h1>Hello!</h1>
        <p>This is the hello page.</p>
        </body>
    </html>
    """
    return html


@app.route("/goodbye")
def say_bye():
    return "good bye"


@app.route("/search")
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1><p>Sorting by: {sort}</p>"
