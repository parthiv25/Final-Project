from flask import Flask

from flask import render_template

from db import get_inventory


app = Flask(__name__)


@app.route('/')
def index():
    # return "Hello World"
    return render_template('index.html', message="Helloll")


@app.route('/view_stock')
def view_stock():
    table = get_inventory()
    # return str(table)
    return render_template('view_stock.html', data=table)
