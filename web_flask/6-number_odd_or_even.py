#!/usr/bin/python3
"""a server starts"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return f'{n} is a number'
    else:
        return 'Not Found', 404

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('6-number_template.html', number=n)
    else:
        return 'Not Found', 404

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if isinstance(n, int):
        number_type = "odd" if n % 2 != 0 else "even"
        return render_template('6-number_odd_or_even.html', n=n, number_type=number_type)
    else:
        return 'Not Found', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
