#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
env = getenv('HBNB_TYPE_STORAGE')


@app.teardown_appcontext
def db_teardown(self):
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
