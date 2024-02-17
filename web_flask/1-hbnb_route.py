#!/usr/bin/python3
"""Start Flask app"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    ''' Index file'''
    return "Hello HBNB!"


@app.route("/hbnb")
def hnb():
    """sub route content"""
    return "HBNB"


if __name__ == "__main__":
    '''Main function'''
    app.run(debug=True, host='0.0.0.0')
