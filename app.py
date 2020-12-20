from flask import Flask

from flask import render_template

from db import get_inventory, write_transcation

from flask import request

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



@app.route('/add_transaction', methods=['POST'])
def add_transaction():

    data = request.form
    trans = []
    # print(request.__dict__)
    # print(data)
    for row in data.keys():
        trans.append([row, int(data[row])])
    print(trans)
    write_transcation(trans)
    return "okayyy"

@app.route('/create_invoice')
def create_invoice():
    table = get_inventory()
    # return str(table)

    return render_template('create_invoice.html', data=table)
