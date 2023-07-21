#!/usr/bin/python3
"""
0-hello_route.py module
"""
from flask import Flask

app = Flask(__name__)

"""Route to display "Hello HBNB!" """


@app.route('/', strict_slashes=False)
def hello():
    """funtion that returns Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
