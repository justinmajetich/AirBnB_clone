#!/usr/bin/python3
# list of states
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states')
def stateList():
    # lists states in html
    return render_template('9-states.html',
                           storage=storage.all('State'), stObj=None)


@app.route('/states/<id>')
def cityStateList(id):
    # lists states in html
    stObj = storage.all('State').get('State.{}'.format(id))
    return render_template('9-states.html', stObj=stObj, storage=None)


@app.teardown_appcontext
def closer(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
