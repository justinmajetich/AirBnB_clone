#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)
app.strict_slashes = False
@app.route('/')
def hello():
    """display Hello HBNB"""
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """display HBNB"""
    return "HBNB"

@app.route('/c/<text>')
def C(text):
    """display “C ” followed by the value of the text variable
        (replace underscore _ symbols with a space"""
    text = text.replace('_', ' ')
    return "C %s" % text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
