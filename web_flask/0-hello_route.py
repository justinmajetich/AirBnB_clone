#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function called with / route """
    return render_template("10-hbnb_filters.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=None)
