from logging import PlaceHolder
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


# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "You made a post request"


# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "You made a get request"

@app.route("/add-comment")
def add_comment_form():
    return """
        <h1>Add Comment</h1>
        <form method="POST">
            <input type="test" placeholder='comment' name="comment"/>
            <input type="test" placeholder='username' name="username"/>
            <button>Submit</button>
        </form>
    """


@app.route("/add-comment", methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
        <h1>Saved your Comment</h1>
        <ul>
            <li>Username: {username}</li>
            <li>Comment: {comment}</li>
        </ul>
    """


@app.route("/r/<subreddit>")
def show_subreddit(subreddit):
    return f"This is a {subreddit}"


@app.route("/r/<subreddit>/comments/<post_id>")
def show_comments(subreddit, post_id):
    return f"""<h1>Viewing comments for post with id: {post_id}
        from the {subreddit}.
    """


POSTS = {
    1: "I like donuts",
    2: "oh yeah",
    3: "lets go",
    4: "YOLO"
}


@app.route("/posts/<int:id>")
def find_post(id):
    post = POSTS.get(id, "Post not found")
    return f"""
        <p>{post}</p>
    """
