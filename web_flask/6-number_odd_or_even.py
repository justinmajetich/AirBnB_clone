#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def c_text(text):
    return "C {}".format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def python_text(text="is cool"):
    return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>')
def text_if_int(n):
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def html_if_int(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>')
def html_odd_or_even(n):
    if n % 2 == 0:
        num_type = 'even'
    else:
        num_type = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, num_type=num_type)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
