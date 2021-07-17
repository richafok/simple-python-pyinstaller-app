import flask
import calc
import sys

app = flask.Flask(__name__)

@app.route('/')
@app.route('/add/<a>/<b>/')
def add(a, b):
    return str(calc.add2(a, b))

if __name__ == '__main__':
    app.run(host='0.0.0.0')