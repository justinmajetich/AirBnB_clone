#!/usr/bin/python3

from flask import Flask
from markupsafe import escape
from flask import render_template


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def routeC(text):
    text = text.replace("_", " ")
    return f'C {escape(text)}'

@app.route('/python', strict_slashes=False)
def routePython1():
    return 'Python is cool'

@app.route('/python/<text>', strict_slashes=False)
def routePython2(text):
    text = text.replace("_", " ")
    if not text:
        text = "is cool"
    return f'Python {escape(text)}'

@app.route('/number/<int:n>', strict_slashes=False)
def routeN(n):
        return f'{n} is a number'

@app.route('/number_template/<int:n>', strict_slashes=False)
def renderHTML(n):
   return render_template('5-number.html', n=n) 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
