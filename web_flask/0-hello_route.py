#!/usr/bin/python3
"""
Flask website with a single paragraph
that says "Hello, HBNB!".

When this script is the main script,
the website is ran and hosted in
"0.0.0.0" in port 5000.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    HTML paragraph with "Hello, HBNB!"
    in it.
    """
    return "<p>Hello HBNB!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
