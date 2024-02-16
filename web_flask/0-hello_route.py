#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask

app = Flask(_name_)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
