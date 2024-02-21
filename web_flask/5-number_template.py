#!/usr/bin/python3
"""Start Flask app"""

from flask import Flask, abort, render_template
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


@app.route("/c/<text>")
def c_fun(text):
    new_string = text.replace('_', ' ')
    return "C " + new_string


@app.route("/python/")
@app.route("/python/<text>")
def py_fun(text='is cool'):
    new_str = text.replace('_', ' ')
    return "Python " + new_str


@app.route("/number/<n>")
def is_number(n):
    try:
        m = int(n)
        return f"{n} is a number"
    except Exception:
        abort(404)


@app.route("/number_template/<n>")
def number_tmp(n):
    try:
        n = int(n)
        return render_template("5-number.html", number=n, page_title=hnb())
    except Exception:
        abort(404)


if __name__ == "__main__":
    '''Main function'''
    app.run(debug=True, host='0.0.0.0')
