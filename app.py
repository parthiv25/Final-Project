from flask import Flask

from flask import render_template

from db import get_inventory, write_transcation

from flask import request

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


@app.route('/add_transaction', methods=['POST'])
def add_transaction():

    data = request.form
    trans = []
    # print(data.keys)
    for row in data.keys():
        trans.append(data[row].split(":"))

    write_transcation(trans)
    return "okayyy"
