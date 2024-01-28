#!/home/wala/AirBnB_clone_v2/venv/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/list')
def item_list():
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', items=items)



if __name__ == '__main__':
    app.run(debug=True)

