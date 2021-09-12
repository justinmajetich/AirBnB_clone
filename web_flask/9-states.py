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


@app.route('/states', strict_slashes=False)
def states_list():
    """
        display state list
    """
    states = __get_obj_list_from_dict(storage.all(State))
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_show(id):
    """
        show state
    """
    state = get_obj("State", id)
    return render_template('9-states.html', state=state)


def get_obj(class_name: str, uuid: str):
    """
        get object from storage
    """
    if "{}.{}".format(class_name, uuid) in storage.all(State):
        return storage.all(State)["{}.{}".format(class_name, uuid)]
    else:
        return None


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
