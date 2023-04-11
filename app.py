from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/twee")
def hello_world2():
    return "<p>Hello, World twee!</p>"
