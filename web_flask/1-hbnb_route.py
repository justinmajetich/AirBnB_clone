from flask import Flask
"""
A simple flask server running on 0.0.0.0:5000
"""

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def display_root():
    """Prints 'Hello HBNB!' to display"""
    # print("Hello HBNB!")
    return "Hello HBNB!"


@app.route('/hbnb')
def display_hbnb():
    """Prints 'HBNB' to display"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
