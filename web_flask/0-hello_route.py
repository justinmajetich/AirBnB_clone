from flask import Flask
"""
A simple flask server running on 0.0.0.0:5000
"""

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """Prints 'Hello HBNB!' to display"""
    # print("Hello HBNB!")
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
