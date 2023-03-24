#!/usr/bin/python3
""" Flask Routing Template """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list',  strict_slashes=False)
def display_states_list():
    """ retrieve list of states and passes to template"""
    # states_list = storage.all("State")
    states_list = []
    dic_states = storage.all(State)
    for state in dic_states.values():
        # for city in dic_cities.values():
        states_list.append(state)
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def teardown_db(exception):
    '''close connections'''
    storage.close()

if __name__ == "__main__":
    app.run()
