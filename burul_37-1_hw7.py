import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def add_products(connection, product_title, quantity, price):
    try:
        cursor = connection.cursor()
        cursor.execute('''Insert INTO products
        (product_title, quantity, price)
        VALUES (?, ?, ?)''', (product_title, quantity, price))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_quantity(connection, product_id, new_quantity):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET quantity = ? WHERE id = ?", (new_quantity, product_id))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def update_product_price(connection, product_id, new_price):
    try:
        cursor = connection.cursor()
        cursor.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product_by_id(connection, product_id):
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def select_products_below_limit(connection, price, quantity):
    try:
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM products WHERE price < ? AND quantity > ?''', (price, quantity))
        products_list = cursor.fetchall()
        for product in products_list:
            print(product)
    except sqlite3.Error as e:
        print(e)

def select_all_products(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM products")
        products_list = cursor.fetchall()
        for product in products_list:
            print(product)
    except sqlite3.Error as e:
        print(e)

def search_products_by_title(connection, keyword):
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products WHERE product_title LIKE ?',
                       ('%' + keyword + '%',))
        products_list = cursor.fetchall()
        for product in products_list:
            print(product)
    except sqlite3.Error as e:
        print(e)

my_connection = create_connection('hw.db')
if my_connection is not None:
    print('Connected to SQLite3 successfully')
    sql_create_table = '''
        CREATE TABLE products (
        id integer primary key autoincrement,
        product_title VARCHAR (200) NOT NULL,
        quantity REAL NOT NULL DEFAULT 0.00,
        price DECIMAL(10,2) NOT NULL DEFAULT 0.00
    )
    '''
    create_table(my_connection, sql_create_table)

add_products(my_connection, 'Bread', 515, 25)
add_products(my_connection, 'Sugar', 1000, 87)
add_products(my_connection, 'Rice', 500, 65)
add_products(my_connection, 'Butter', 200, 115)
add_products(my_connection, 'Cheese', 200, 105)
add_products(my_connection, 'Buckwheat', 300, 120)
add_products(my_connection, 'Pasta', 100, 70)
add_products(my_connection, 'Beef', 750, 500)
add_products(my_connection, 'Chicken beef', 550, 350)
add_products(my_connection, 'Flour', 3050, 35)
add_products(my_connection, 'Milk', 250, 68)
add_products(my_connection, 'Sausages', 350, 497)
add_products(my_connection, 'Fish', 250, 2000)
add_products(my_connection, 'Juice', 250, 115)
add_products(my_connection, 'Cigarette', 600, 200)
update_product_quantity(my_connection, 800, 85)
delete_product_by_id(my_connection, 5)
select_all_products(my_connection)
select_products_below_limit(my_connection, 100, 500)
search_products_by_title(my_connection, 'rice')

my_connection.close()
