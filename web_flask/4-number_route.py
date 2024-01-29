#!/usr/bin/python3
"""Servivcio Web con Flask"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
# Define una funcion home y retorna la cadena Hello HBNB
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
        return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def mostrar_c(text):
    # Reemplaza los símbolos de subrayado (_) con un espacio
    cleaned_text = text.replace('_', ' ')
    return f'C {cleaned_text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def mostrar_py(texto='is cool'):
    """Mensaje Python si es genial!!!"""
    # Reemplaza los símbolos de subrayado (_) con un espacio
    cleaned_text = text.replace('_', ' ')
     return f'Python {cleaned_text}'

 @app.route('/number/<int:n>', strict_slashes=False)
 def number_router(n):
     if isinstance(n, int):
         return f'{n} is a number'


 if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
