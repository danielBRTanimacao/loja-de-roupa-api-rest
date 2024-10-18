from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/list")
def hello_world():
    with open('json/list.json', 'r') as file:
        data = json.load(file)

    return f"<p>{data}</p>"

app.run()