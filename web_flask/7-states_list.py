#!/usr/bin/python3
"""
script that starts a Flask web application

Your web application must be listening on 0.0.0.0, port 5000

You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage
    and
    storage.all(...)

Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>:
    display “C ” followed by
    the value of the text variable
        (replace underscore _ symbols with a space )
/python/<text>:
    display “Python ”, followed by
    the value of the text variable
        (replace underscore _ symbols with a space )
    default value of text is “is cool”

/number/<n>:
    display “n is a number”
        only if n is an integer
        replace "n" with the int given

/number_template/<n>:
    display a HTML page only if n is an integer
        this page is a separate file called 5-number.html
        H1 tag: “Number: n” inside the tag BODY

/number_odd_or_even/<n>:
    display a HTML page only if n is an integer:
        this page is a separate file called 6-number_odd_or_even.html
        H1 tag: “Number: n is even|odd” inside the tag BODY
You must use the option strict_slashes=False in your route definition.
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_():
    """if rout as above,
    returns as below
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """if rout as above,
    returns as below
    """
    return 'HBNB'


@app.route('/c/<text>')
def hello_c_text(text=''):
    """if rout as above,
    returns as below
    """
    edited = text.replace('_', ' ')
    return 'C ' + edited


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def hello_python_text(text='is cool'):
    """if rout as above,
    returns as below
    """
    edited = text.replace('_', ' ')
    return 'Python ' + edited


@app.route('/number/<int:n>')
def hello_number(n=0):
    """if n is int, return it is a number
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def hello_number_template(n=0):
    """if n is int, return a webpage
    said webpage is in another file
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def hello_odd_even(n=0):
    """if n is int, return a webpage
    said webpage is in another file
    """
    polarity = 'odd'
    if n % 2 == 0:
        polarity = 'even'
    return render_template('6-number_odd_or_even.html', n=n, polarity=polarity)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
