from flask import *
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})

app_name = "Stack Notify Admin"


@app.route('/')
@cross_origin()
def index():
    return render_template('index.html', app_name=app_name)


if __name__ == '__main__':
    app.run(host="192.168.0.102", port=3200)
