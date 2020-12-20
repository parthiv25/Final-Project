from flask import Flask

from flask import render_template

from db import get_inventory, write_transcation

from flask import request

from db import add_item_sql


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


@app.route('/add_item')
def add_item():

    return render_template('add_item.html')


@app.route('/add_item_sql', methods=['POST'])
def add():

    # print(request.form)
    name = request.form['item_name']
    quan = int(request.form['quantity'])
    add_item_sql(name, quan)
    return f"Added {name} : {quan} successfully"
    # return "okay"


@app.route('/add_transaction', methods=['POST'])
def add_transaction():

    data = request.form
    trans = []
    # print(request.__dict__)
    # print(data)
    for row in data.keys():
        trans.append([row, int(data[row])])
    print(trans)
    t_id = write_transcation(trans)
    return f"Your transaction id is {t_id}"


@app.route('/create_invoice')
def create_invoice():
    table = get_inventory()
    # return str(table)

    return render_template('create_invoice.html', data=table)

@app.route('/view_invoice')
def view_invoice():
    table = get_inventory()
    # return str(table)

    return render_template('view_invoice.html', data=table)
