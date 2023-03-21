#!/usr/bin/python3
from flask import Flask
from models import storage, State
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """display a HTML the States"""
    all_states = list(storage.all(State).values())
    return (render_template('7-states_list.html', all_states=all_states))


@app.teardown_appcontext
def teardown(self):
    """function that call close methofd"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
