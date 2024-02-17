#!/usr/bin/python3
"""Creating Flask module"""
from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False

@app.route("/")
def hello():
    """Printing just text to the browser"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Main function setting hot to be open for other computers"""
    app.run(debug=True, host='0.0.0.0')
