#!/usr/bin/python3
'''
Start a Flask web application
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''
    site index
    '''
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
