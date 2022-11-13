#!/usr/bin/python3
"""starts a Flask web application."""


from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def helloHBNB():
    """returns Hello HBNB!."""
    return ("Hello HBNB!")


@app.route("/hbnb")
def HBNB():
    """returns HBNB."""
    return ("HBNB")


@app.route("/c/<text>")
def variableValue(text):
    """returns the value of a variable."""
    return (
        'C %s' % escape(text.replace("_", " "))
    )


@app.route("/python")
@app.route("/python/<text>")
def retPython(text="is cool"):
    """Display Python.

    Followed by the value of the text.
    """
    return (
        "Python %s" % escape(text.replace("_", " "))
    )


@app.route("/number/<int:n>")
def isInt(n):
    """Display Int.

    Display the value of n if only is int.
    """
    return ("{} is a number".format(
        n
    ))


@app.route(
    "/number_template/<int:n>"
)
def numberTempate(n):
    """Renders a template if n is int."""
    return render_template(
        "5-number.html", n=n
    )


@app.route("/number_odd_or_even/<int:n>")
def evenOdd(n):
    """Returns even or odd."""
    def getType(num):
        """Returns type."""
        if (num % 2 == 0):
            return ("even")
        else:
            return ("odd")
    typeNum = getType(n)
    return render_template(
        "6-number_odd_or_even.html", n=n, get_type=typeNum
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
