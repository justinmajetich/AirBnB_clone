#!/usr/bin/python3
"""
Script that starts a Flask web application
    - listening on 0.0.0.0, port 5000
    - display “Hello HBNB!”
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb_route():
    """Method that displays Hello HBNB!"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
