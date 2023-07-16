#!/usr/bin/python3
"""
Write a script that starts a Flask web application.
The application must be listening on 0.0.0.0, port 5000

Routes:
- /: display "Hello HBNB!"

Note: You must use the option 'strict_slashes=Flase in the route definition
"""


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=Flase)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
