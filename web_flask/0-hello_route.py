#!/usr/bin/python3
""" connect flask """

from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)


# Définir une route pour l'URL racine '/'
@app.route("/")
def hello():
    strict_slashes = False # Désactiver la redirection automatique vers une URL avec une barre oblique à la fin
    return 'Hello HBNB!' # Retourner une chaîne de caractères en réponse à la requête HTTP


# Exécuter l'application si le script est exécuté directement (pas importé)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) # Lancer l'application sur l'adresse IP 0.0.0.0 et le port 5000

