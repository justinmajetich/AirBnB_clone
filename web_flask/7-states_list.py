#!/usr/bin/python3
""" starting a flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ storage to fetch data from the storage engine 
    remove current SQL Alchemy"""
    states = storage.all(states)
    dic_html = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html', 
                           Table="States", 
                           items =dic_html)
    

@app.teardown_appcontext
def end_session(excep):
    """ close session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

