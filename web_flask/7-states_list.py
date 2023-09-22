#!/usr/bin/python3
"""
    A script that starts a Flask web application listening
    on 0.0.0.0, port 5000 with Routes:
    [/states_list]: display a HTML page
"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def statesList():
    """ A function that lists all states records """
    states = storage.all("State")

    return render_template('7-states_list.html',Table="States" ,states=states)


if __name__ == '__main__':
    """ Run module only then ran """
    app.run(host='0.0.0.0', port=5000)
