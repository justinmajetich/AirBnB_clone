#!/usr/bin/python3
"""Corriendo el servicio web con Flask"""

# Importa la clase Flask
from flask import Flask

# Crea una instancia de la clase Flask llamada app
app = Flask(__name__)


# Define una ruta / y llama a la funcion home
# strict_slashes permite que la ruta coincida con barras diagonales
@app.route("/", strict_slashes=False)
# Define una funcion home y retorna la cadena Hello HBNB!
def home():
    return "Hello HBNB!"


# Esta funcion asegura que este script de Flask solo se ejecute
# cuando ejecutas este script directamente y no cuando importas
# como un modulo
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
