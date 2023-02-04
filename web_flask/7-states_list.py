#!/usr/bin/python3
""" Program that starts a Flask web application and list the states
Your web application must be listening on 0.0.0.0, port 5000
In Routes /states_list: display a HTML page: (inside the tag BODY)"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(self):
    """use storage for fetching data from the storage engine
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_info():
    """Display a HTML page inside the tag BODY"""
    return render_template('7-states_list.html',
                           states=storage.all(State))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
