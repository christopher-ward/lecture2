from flask import Flask
#application.py is typically what the file calling Flask would look like.

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"
    #could also do
    #return f"<h1>Hello, {name}!<h1>"
