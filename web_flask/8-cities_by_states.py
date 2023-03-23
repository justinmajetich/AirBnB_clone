#!/usr/bin/python3

"""This module starts a Flask web application to display States and Cities."""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_route():
    """Renders a template to display all states and their cities."""
    states_dict = storage.all(State)
    city_list = storage.all(City).values()
    states_list = list(states_dict.values())
    sorted_states_list = sorted(states_list, key=lambda x: x['name'])
    for i in sorted_states_list:
        cities = [d for d in city_list if d['state_id'] == i['id']]
        i['cities'] = sorted(cities, key=lambda x: x['name'])
    return render_template('8-cities_by_states.html',
                           states=sorted_states_list)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
