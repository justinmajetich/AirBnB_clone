#!/usr/bin/python3
""" connect flask """

from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)


# Définir une route pour l'URL racine '/'
@app.route("/")
def hello():
    # Désac la redirection auto vers une URL avec une barre oblique à la fin
    strict_slashes = False
    # Retourner une chaîne de caractères en réponse à la requête HTTP
    return 'Hello HBNB!'


# Exécuter l'application si le script est exécuté directement (pas importé)
if __name__ == '__main__':
    # Lancer l'application sur l'adresse IP 0.0.0.0 et le port 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
