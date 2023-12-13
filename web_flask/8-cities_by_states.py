#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Route taht displays the html page of
    a list of states objects sorted by name
    """
    states_li = storage.all(State).values()
    return render_template('7-states_list.html', states=states_li)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Route that display a HTML page with a list of cities
    objects sorted by name """
    city_li = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=city_li)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """After each request, remove the SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
