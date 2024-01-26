#!/usr/bin/python3
"""Servivcio Web con Flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def mostrar_c(texto):
    # Reemplaza los símbolos de subrayado (_) con un espacio
    texto_con_espacios = texto.replace('_', ' ')
    return f'C {texto_con-espacios}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
