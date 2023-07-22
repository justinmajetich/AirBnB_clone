#!/usr/bin/python3
'''
0-hello_route module
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_wordl():
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
