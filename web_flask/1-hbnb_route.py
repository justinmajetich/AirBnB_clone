#!/usr/bin/python3
'''
    a python script that a flask web application
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_word():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port='5000')
