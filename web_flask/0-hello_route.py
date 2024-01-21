#!/usr/bin/python3
"""Corriendo el servicio web con Flask"""

from flask import Flask

"""Crea una instancia de la clase Flask llamada app"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
# Define una funcion home y retorna la cadena Hello HBNB
def hello_hbnb():
    return "Hello HBNB!"


if __name__ == "__main__":
    # Esta funcion asegura que este script de Flask solo se ejecute
    # cuando ejecutas este script directamente y no cuando importas
    # como un modulo
    app.run(host='0.0.0.0', port=5000)
