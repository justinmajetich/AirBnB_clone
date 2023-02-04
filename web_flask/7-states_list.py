#!/usr/bin/python3
""" Program that starts a Flask web application and list the states
Your web application must be listening on 0.0.0.0, port 5000
In Routes /states_list: display a HTML page: (inside the tag BODY)"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """  Function that display a HTML page """
    # Fetch in a list of all the values available in a given dictionary
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def remove_session(exception):
    """ After each request you must remove the current SQLAlchemy Session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
