#!/usr/bin/python3
""" This script that starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Route that display a HTML page with a list of states
    objects sorted by name """
    state_li = storage.all(State).values()
    return render_template('7-states_list.html', states=state_li)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Route that display a HTML page with a list of cities
    objects sorted by name """
    city_li = storage.all(State).values()
    return render_template('8-cities_by_states.html', cities=city_li)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    state_dic = storage.all(State)
    state = None
    for obj in state_dic.values():
        if obj.id == id:
            state = obj
    return render_template('9-states.html', states=state_dic, id=id,
                           state=state)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """ Function that removes the current SQL Alchemy Session after each
    request. """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
