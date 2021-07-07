#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(self):
    """ close storage """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Display a HTML page: showing the cities by states"""
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
