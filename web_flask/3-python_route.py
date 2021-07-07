#!/usr/bin/python3
""" this module starts a flask aplication """


from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def Hello_HBNB():
   return 'Hello HBNB!'

@app.route('/hbnb')
def HBNB():
   return 'HBNB'


@app.route('/c/<text>')
def show_c(text):
   print(type(text))
   return ('C ' + text.replace('_', ' '))

@app.route('/python/<text>')
@app.route('/python/')
def show_python(text='is cool'):
   return ('Python ' + text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True)
