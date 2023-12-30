#!/usr/bin/python3
"""Start Flask app"""
from flask import Flask, render_template
import storage
from models.state import State


app = Flask(__name__)

@app.teardown_appcontext
def close():
    """Close down the session"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def state_list():
    """States Route"""
    states = storage.all(state)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
