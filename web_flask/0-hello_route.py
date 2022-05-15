#!/usr/bin/python3
"""Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    ou must use the option strict_slashes=False in your route definition
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Print Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
