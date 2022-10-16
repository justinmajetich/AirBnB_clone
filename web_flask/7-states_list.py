#!/usr/bin/python3
""" Script that runs a Flask app """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def closing(error):
    """closes session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """ function that returns text"""
    state = storage.all()
    return render_template('7-states_list.html', state=state)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
