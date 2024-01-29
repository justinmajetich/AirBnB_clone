#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)
app.config['DEBUG'] = False

@app.route("/")
def hello():
        return "Hola, mundo!"
