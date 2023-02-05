#!/usr/bin/python3
""" starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes: /: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """returning  Hello HBNB str"""
    return("Hello HBNB!")

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returning  HBNB str"""
    return("HBNB!")

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )"""
    return "C {}".format(text.replace("_", " "))

app.route("/python", strict_slashes=False)
app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """display “ python” followed by the value of the text variable (replace underscore _ symbols with a space )"""
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:number>", strict_slashes=False)
def number(numb):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(numb)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)