#!/usr/bin/python3
""" 7. Start flask service that does something. """

from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


#@app.route()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
