#!/usr/bin/python3
"""
    A script that starts a Flask web application listening
    on 0.0.0.0, port 5000 with Routes:
    [/states_list]: display a HTML page
"""

from models import *
from models import storage
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def statesList():
    """ A function that lists all states records """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_bg(exception):
    storage.close()



if __name__ == '__main__':
    """ Run module only then ran """
    app.run(host='0.0.0.0', port=5000)
