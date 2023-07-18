#!/usr/bin/python3
"""
script that starts a Flask web application

Your web application must be listening on 0.0.0.0, port 5000

You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage
    and
    storage.all(...)

Routes:

    /states_list: display a HTML page:
        inside tag body:
            H1 tag: “States”
            UL tag:
                with the list of
                    all State objects present in DBStorage
                        sorted by name (A->Z)
                LI tag:
                description of one State:
                    <state.id>: <B><state.name></B>

You must use the option strict_slashes=False in your route definition.
"""

from flask import Flask, render_template
app = Flask(__name__)
from models import storage


@app.route('/number_odd_or_even/<int:n>')
def hello_odd_even(n=0):
    """this module needs to be updated
    to perform task 8
    """
    polarity = 'odd'
    if n % 2 == 0:
        polarity = 'even'
    return render_template('6-number_odd_or_even.html', n=n, polarity=polarity)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
