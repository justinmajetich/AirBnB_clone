#!/usr/bin/python3
"""
"""
from flask import Flask

app = Flask(__name__)
app.strict_slashes = False
@app.route('/')
def hello():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def C(text):
    text = text.replace('_', ' ')
    return "C %s" % text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
