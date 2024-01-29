#!/usr/bin/python3
"""Servivcio Web con Flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def mostrar_c(text):
    # Reemplaza los símbolos de subrayado (_) con un espacio
    cleaned_text = text.replace('_', ' ')
    return f'C {cleaned_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
