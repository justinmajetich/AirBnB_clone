#!/usr/bin/python3
"""
Script that starts a Flask web application
    - listening on 0.0.0.0, port 5000
    - /: display “Hello HBNB!”
    - /hbnb: display "HBNB"
    - /c/<text>: display “C ” followed by the value of the text variable
    - /python/(<text>): display “Python ”,
      followed by the value of the text variable
        * The default value of text is “is cool”
    - /number/<n>: display “n is a number” only if n is an integer
    - /number_template/<n>: display a HTML page only if n is an integer:
        * H1 tag: “Number: n” inside the tag BODY
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb_route():
    """Method that displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """Method that displays HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Method that displays 'C' with <text>"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Method that displays 'python' with <text>"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Method that displays 'n is a number' if n is an integer"""
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Method that displays a HTML page if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
