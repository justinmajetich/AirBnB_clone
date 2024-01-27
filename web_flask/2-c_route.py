#!/usr/bin/python3
"""starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def disp_hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Display  c follwed by the value text"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
