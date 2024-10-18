from flask import Flask, render_template, make_response
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/roupas", methods=['GET', 'POST'])
def clothes():
    with open('json/list.json', 'r') as file:
        data = json.load(file)

    return make_response(data)

app.run(debug=True)