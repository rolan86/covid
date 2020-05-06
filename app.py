import json

from flask import Flask

from data_script import get_day_one


app = Flask(__name__)

@app.route('/')
def index():
    return "Healthy"

@app.route('/dayone')
def by_country():
    return json.dumps(get_day_one("canada"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
