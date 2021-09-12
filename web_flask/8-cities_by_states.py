#!/usr/bin/python3
"""
    script that starts a Flask web application
"""

from flask import Flask, escape, request, render_template
from models import storage
from models.state import State

# creates instance of Flask, app is bound to gunicorn when running app server
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
        remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
        display state list
    """
    states = __get_obj_list_from_dict(storage.all(State))
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state_list():
    """
        display cities by state
    """
    states = __get_obj_list_from_dict(storage.all(State))
    return render_template('8-cities_by_states.html', states=states)


def __get_obj_list_from_dict(obj_dict: dict):
    """
        Transform an object dictionary to an object list
    """
    obj_list = []
    for key, obj in obj_dict.items():
        obj_list.append(obj)

    return obj_list


if __name__ == '__main__':
    # runs the Flask application through port 5000 from local host
    app.run(host='0.0.0.0', port='5000')
