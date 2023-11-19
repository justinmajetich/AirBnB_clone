#!/usr/bin/python3
""" Set up for Flask app """


from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns this string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def ello():
    """Returns this string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ello_puppet(text):
    """Returns this string"""
    processed_text = text.replace('_', ' ')
    return f"C {processed_text}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ello_python(text):
    """Returns this string"""
    processed_text = text.replace('_', ' ')
    return f"Python {processed_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Returns if n is an integer """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays HTML if n is an integer """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    abort(404)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Displays HTML if n is an integer """
    if isinstance(n, int):
        parity = "even" if n % 2 == 0 else "odd"
        return render_template('6-number_odd_or_even.html', n=n, parity=parity)
    abort(404)


""" Setting the localhost and port """
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
