#!/usr/bin/python3
"""starts a Flask web application"""
from models import Storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """ returns html page with list of States """
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown():
    """ removes currents SQLAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
