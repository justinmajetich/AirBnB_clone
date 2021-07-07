#!/usr/bin/python3
""" this module starts a flask aplication """


from flask import Flask, render_template
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

@app.route('/number/<int:n>')
def show_number(n):
   if type(n) is int:
      return (str(n) + ' is a number')

@app.route('/number_template/<int:n>')
def show_numberhtml(n):
   if type(n) is int:
      return (render_template('5-number.html', n=n))

@app.route('/number_odd_or_even/<int:n>')
def show_number_odd(n):
   if type(n) is int:
      return (render_template('6-number_odd_or_even.html', n=n))

if __name__ == '__main__':
   app.run(debug=True)
