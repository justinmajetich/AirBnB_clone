#!/usr/bin/python3
""" A script that starts a flask web application"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays a HTML page with a list of states """
    states = storage.all(State)
    return render_template('7-states_list.html')

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
