#!/usr/bin/python3
"""Import data from mysql"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes(False)


@app.teardown_appcontext()
def close_sessions():
    '''After each request you must remove the current SQLAlchemy Session'''
    storage.close()

@app.route('/states_list')
def list_state():
    state_list = storage.all(State);
    return render_template('7-7-states_list.html', states=state_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0.0')

