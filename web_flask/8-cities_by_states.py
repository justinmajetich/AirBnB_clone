#!/usr/bin/python3
""" Script that runs a Flask app """
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def closing(error):
    """closes session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def city():
    """ function that returns text"""
    state = storage.all('State')
    return render_template('8-cities_by_states.html', state=state)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
