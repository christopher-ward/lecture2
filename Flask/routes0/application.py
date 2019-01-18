from flask import Flask
#application.py is typically what the file calling Flask would look like.

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/david")
def david():
    return "Hello, David!"

@app.route("/maria")
def maria():
    return "Hello, Maria!"
