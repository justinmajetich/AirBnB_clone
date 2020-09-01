#!/usr/bin/python3
""" this module starts a flask aplication """


from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_HBNB():
   return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(debug=True)
