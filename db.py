import sqlite3


def get_inventory():

    conn = sqlite3.connect('inventory.db')
    cursor = conn.execute("SELECT * FROM inventory")
    table = cursor.fetchall()
    conn.close()
    print(table)
    return table


def add_item(name, quantity):

    conn = sqlite3.connect('inventory.db')

    cursor = conn.execute("SELECT * FROM inventory")

    sr_no = cursor.fetchall()[-1][0] + 1

    cursor = conn.execute(
        f"INSERT INTO inventory values ({sr_no}, '{name}', {quantity}) ")
    # print(cursor.fetchall())
    conn.commit()
    conn.close()
    return


# add_item("test3", 0)
# get_inventory()
