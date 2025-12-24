#!/usr/bin/python3
""" Start flask application
    Must be listening on 0.0.0.0, port 5000
routes:
     /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>
              Replace underscore _ symbols with a space
    /python/<text>: display “Python ”, followed by the value of <text>
              Replace underscore _ symbols with a space
              The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
              H1 tag: “Number: n” inside the tag BODY
    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
              H1 tag: “Number: n is even|odd” inside the tag BODY

"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    converter = text.replace('_', ' ')
    return f'C {converter}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text='is cool'):
    converter = text.replace('_', ' ')
    return f'Python {converter}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
