from flask import Flask
#application.py is typically what the file calling Flask would look like.

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"
