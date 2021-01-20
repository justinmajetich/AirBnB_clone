#!/usr/bin/python3
"""
Experimenting with flask
"""
from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def ripandtear(_):
    """Rips and tears
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def lists(id=None):
    """State list
    """
    lili = storage.all(State)
    if id:
        try:
            single = lili['State.' + id]
            return render_template('9-states.html', single=single)
        except KeyError:
            return render_template('9-states.html', single=1)
    else:
        return render_template('9-states.html', states=list(lili.values()))

if __name__ == '__main__':
    storage.reload()
    app.run('0.0.0.0', 5000)
