from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/techDetails")
def techDetails():
    return "<p> Travel and culture blog. Written in Flask, a Python web development platform </p>"
