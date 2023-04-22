#!/usr/bin/python3
"""
Make web app listen on port 5000 and host 0.0.0.0
"""
from flask import Flask

app = Flask('__name__')

@app.route('/', strict_slashes=False)
def hello():
    """ Display Hello HBNB"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
