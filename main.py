# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, Response, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

name = "Stack Notify"

@app.route('/')
@cross_origin()
def index():
    return f"<h1> Welcome to {name} your highness </h1>"

if __name__ == '__main__':
    app.run(host="192.168.0.102", port=3200)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
