#!/usr/bin/python3
""" this module starts a flask aplication """


from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_HBNB():
   return 'Hello HBNB!'

@app.route('/hbnb')
def HBNB():
   return 'HBNB'


@app.route('/c/<text>')
def show_text(text):
   print(type(text))
   return ('C ' + text.replace('_', ' '))

if __name__ == '__main__':
    app.run(debug=True)
