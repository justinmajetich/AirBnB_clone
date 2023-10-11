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
    data = sorted(list(storage.all("State").values()), key=lambda x: x.name)

    return render_template('7-states_list.html', states=data)


@app.route('/hbnb_filters', strict_slashes=False)
def page6():
    """ display a HTML page like 6-index.html """
    return render_template('10-hbnb_filters.html')


@app.route('/hbnb', strict_slashes=False)
def page8():
    """ display a HTML page like 8-index.html """
    return render_template('100-hbnb.html')


@app.teardown_appcontext
def close_db(exception):
    storage.close()


if __name__ == '__main__':
    """ Run module only then ran """
    app.run(host='0.0.0.0', port=5000)
