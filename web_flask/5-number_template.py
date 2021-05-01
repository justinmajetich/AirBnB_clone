#!/usr/bin/python3
"""
starts a Flask web application listening on 0.0.0.0, port 5000
Routes:
        - /: display “Hello HBNB!”
        - /hbnb: display “HBNB”
        - /c/<text>: display “C ” followed by the value of the
                     text variable (replace underscore _ symbols with a space )
        - /python/(<text>): display “Python ”, followed by the value of text
                            variable(replace underscore _ symbols with a space)
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
        """Display 'Hello HBNB!'"""
        return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        """Display 'HBNB'"""
        return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
        """Display C followed by text"""
        return "C %s" % text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
        """Display python followed by text"""
        return "Python %s" % text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
        """Display n is a number, ony if n is number"""
        return "%d is a number" % int(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template(n):
        """Display HTML page only if n is a number"""
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
