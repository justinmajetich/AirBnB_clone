#!/usr/bin/python3
""" script that starts a Flask web application:
    Your web application must be listening on 0.0.0.0, port 5000
    Routes: 1- /: display “Hello HBNB!”
            2- /hbnb: display “HBNB”
            3- /c/<text>: display “C ” followed by the value of the text
                variable (replace underscore _ symbols with a space )
            4- /python/(<text>): display “Python ”, followed by the value of...
                the text variable (replace underscore _ symbols with a space )
                The default value of text is “is cool”
    You must use the option strict_slashes=False in your route definition """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ hello_hbnb method """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def only_hbnb():
    """ only_hbnb method: """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def only_c(text):
    """ only_c method: route to return C followed by text variable, replaces _
        with spaces """
    text = text.replace('_', ' ')
    return ('C' + ' ' + text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<path:text>', strict_slashes=False)
def only_python(text=None):
    """ only_python method: route to return text follow by "is cool"
        (can be overwritten), replaces _ with spaces """
    if text is None:
        text = 'is cool'
    else:
        text = text.replace('_', ' ')
    return ('Python' + ' ' + text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
