#!/usr/bin/python3
""" connect flask """

from flask import Flask, render_template
from markupsafe import escape

# Créer une instance de l'application Flask
app = Flask(__name__)


# Définir une route pour l'URL racine '/'
@app.route("/", strict_slashes=False)
def hello():
    # Retourner une chaîne de caractères en réponse à la requête HTTP
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = f"C {(text)}"
    return text.replace("_", " ")


@app.route('/python/', strict_slashes=False, defaults={"text": "is cool"})
# Définition de la première route, qui affiche "Python is cool" par défaut
@app.route('/python/<text>', strict_slashes=False)
# seconde route, permet de spécifier un texte à afficher à la place de is cool
def python_text(text):
    text = f"Python {text}"
    return text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f"{n} is a number"


# Définition de la route "/number_template/" qui prend un entier n en paramètre
@app.route('/number_template/<int:n>', strict_slashes=False)
def render_t(n):
    # Rendu du template "5-number.html" en passant la valeur de n en paramètre
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_t2(n):
    return render_template('6-number_odd_or_even.html', n=n)


# Exécuter l'application si le script est exécuté directement (pas importé)
if __name__ == '__main__':
    # Lancer l'application sur l'adresse IP 0.0.0.0 et le port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
