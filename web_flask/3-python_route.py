#!/usr/bin/python3
""" Web application listening on 0.0.0.0, port 5000 """
from flask import Flask
""" Import Flask"""

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Display HBNB! """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Display prompt """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False) 
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """
    Display 'Python' followed by the value of text
    Replace underscore _ symbols with a space
    """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
