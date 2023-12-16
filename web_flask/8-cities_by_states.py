#!/usr/bin/python3
"""
starts a Flask web application listening on
0.0.0.0, port 5000 and routes /: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display "C" + text (replaces underscores with spaces)
/python/(<text>): display "Python" + text (default is 'is cool')
/number/<n>: display "n is a number" only if n is an integer
/number_template/<n>: display HTML page only if n is an integer
/number_odd_or_even/<n>: display HTML page only if n is an integer
/state_list: display HTML page with list of all State objects
/cities_by_states: display HTML page with list of all City objects
"""
from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """display text"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """display text"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """display custom text given
       first route statement ensures it works for:
          curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
          curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """display text only if int given"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def html_if_int(n):
    """display html page only if int given
       place given int into html template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def html_odd_or_even(n):
    """display html page only if int given
       place given int into html template
       substitute text to display if int is odd or even
    """
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           n=n, odd_or_even=odd_or_even)


@app.teardown_appcontext
def teardown_db(exception):
    """after each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """display html page
       fetch sorted states to insert into html in UL tag
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """display a HTML page with list of all State objects and their cities"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
