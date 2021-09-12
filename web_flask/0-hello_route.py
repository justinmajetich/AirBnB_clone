#!/usr/bin/python3
"""
    script that starts a Flask web application
"""

from flask import Flask, escape, request

# creates instance of Flask, app is bound to gunicorn when running app server
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        First route
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    # runs the Flask application through port 5000 from local host
    app.run(host='0.0.0.0', port='5000')
