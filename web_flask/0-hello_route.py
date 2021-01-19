#!/usr/bin/python3
"""Hello Flask!"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Hello Holberton"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    """Initial"""
    app.run(host='0.0.0.0', port=5000)
