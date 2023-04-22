#!/usr/bin/python3
"""
Write a script that starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)
app.strict_slashes = False
@app.route('/')
def hello():
    """ display Hello HBNB! """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """ display HBNB"""
    return "HBNB"

@app.route('/c/<text>')
def C(text):
    """
    display “C ” followed by the value of the
    text variable (replace underscore _ symbols with a space
    """
    text = text.replace('_', ' ')
    return "C %s" % text

@app.route('/python')
@app.route('/python/<text>')
def Python(text="is cool"):
    """
    display “Python ”, followed by the value of the 
    text variable (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return "Python %s" % text

@app.route('/number/<int:n>')
def number(n):
    """Display n is a number"""
    return "%s is a number" % n

@app.route('/number_template/<int:n>')
def number_temp(n):
    """Display page of html having the variable n"""
    return render_template("5-number.html", number=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Display Number: n is even|odd"""
    return render_template("6-number_odd_or_even.html", number=n)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
