#!/usr/bin/python3
"""
script that starts a flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    display Hello HBNB
    """
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def hnb_route():
    """
    display HBNB
    """
    return ("HBNB")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
