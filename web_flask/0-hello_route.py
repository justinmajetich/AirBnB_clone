#!/usr/bin/python3
"""
This is a script that starts a Flask web application.
"""
from flask import Flask


""" Name tells to look for resources."""
app = Flask(__name__)

""" Decorator to tell Flask what URL should trigger our function. """
@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'

""" Prevents the Flask development server from starting if the script is imported elsewhere. """
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
