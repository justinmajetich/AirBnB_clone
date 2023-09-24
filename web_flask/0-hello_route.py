#!/usr/bin/python3
"""
This scripts starts a Flask webAPP
listen on 0.0.0.0 on port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
