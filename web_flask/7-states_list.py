#!/usr/bin/python3
""" starting a flask application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ storage to fetch data from the storage enginee """
    """remove current SQL Alchemy"""
    states = sorted(list(storage.all(State).values()), 
                    key=lambda state: state.name)
    
    # print states
    return render_template('7-states_list.html', states=states)

# end session after every request


@app.teardown_appcontext
def end_session(excep):
    """ close session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

