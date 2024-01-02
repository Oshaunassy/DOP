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

def add_countries(connection, country_title):
    try:
        cursor = connection.cursor()
        cursor.execute('''Insert INTO countries
        (title)
        VALUES (?)''', (country_title,))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def add_cities(connection, title, area, country_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''Insert INTO cities
        (title, area, country_id)
        VALUES (?, ?, ?)''', (title, area, country_id))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def add_students(connection, first_name, last_name, city_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''Insert INTO students
        (first_name, last_name, city_id)
        VALUES (?, ?, ?)''', (first_name, last_name, city_id))
        connection.commit()
    except sqlite3.Error as e:
        print(e)

def display_cities(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT id, title FROM cities")
        cities = cursor.fetchall()
        if cities:
            print("Список городов:")
            for city_id, city_title in cities:
                print(f"{city_id}: {city_title}")
        else:
            print("В базе данных нет городов.")
    except sqlite3.Error as e:
        print(e)


def display_students_by_city_id(connection, city_id):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT distinct s.first_name, s.last_name, c.title AS country, ci.title AS city, ci.area
            FROM students s
            JOIN cities ci ON s.city_id = ci.id
            JOIN countries c ON ci.country_id = c.id
            WHERE ci.id = ?
        """, (city_id,))
        students = cursor.fetchall()
        if students:
            print(f"Студенты в выбранном городе:")
            for first_name, last_name, country, city, area in students:
                print(f"Имя: {first_name}, Фамилия: {last_name}, Страна: {country}, Город: {city}, Площадь города: {area}")
        else:
            print("Студенты в выбранном городе не найдены.")

    except sqlite3.Error as e:
        print(e)



my_connection = create_connection('hw.db')
if my_connection is not None:
    print('Connected to SQLite3 successfully')
    sql_create_table_countries = '''
        CREATE TABLE IF NOT EXISTS countries (
        id integer primary key autoincrement,
        title VARCHAR (200) NOT NULL
    )
    '''
    create_table(my_connection, sql_create_table_countries)
    add_countries(my_connection, 'Kyrgyzstan')
    add_countries(my_connection, 'Germany')
    add_countries(my_connection, 'Chine')

    sql_create_cities = '''
        CREATE TABLE IF NOT EXISTS cities (
        id integer primary key autoincrement,
        title VARCHAR (200) NOT NULL,
        area decimal not null default 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
    '''
    create_table(my_connection, sql_create_cities)
    add_cities(my_connection, 'Bishkek', 127, 1)
    add_cities(my_connection, 'Berlin', 891.8, 2)
    add_cities(my_connection, 'Shan-hay', 16410, 3)
    add_cities(my_connection, 'Osh', 182, 1)
    add_cities(my_connection, 'Karakol', 52.53, 1)
    add_cities(my_connection, 'Frankfurt-an-Maine', 248.31, 2)
    add_cities(my_connection, 'Guangzhou', 7434.4, 3)

    sql_create_students = '''
        CREATE TABLE IF NOT EXISTS students (
        id integer primary key autoincrement,
        first_name VARCHAR (50) NOT NULL,
        last_name VARCHAR (50) NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
    '''

    create_table(my_connection, sql_create_students)
    add_students(my_connection, 'Askar', 'Bakirov', 1)
    add_students(my_connection, 'Henry', 'Freeman', 2)
    add_students(my_connection, 'Shao', 'Leen', 3)
    add_students(my_connection, 'Arthur', 'Osmonov', 4)
    add_students(my_connection, 'Nicole', 'Kidman', 5)
    add_students(my_connection, 'Ostap', 'Bender', 6)
    add_students(my_connection, 'Pavel', 'Nikiforov', 7)
    add_students(my_connection, 'Mark', 'Oma', 1)
    add_students(my_connection, 'Anna', 'McCanly', 2)
    add_students(my_connection, 'Tay', 'Nyan', 3)
    add_students(my_connection, 'Bakyt', 'Aydarov', 4)
    add_students(my_connection, 'Marya', 'Nicol', 5)
    add_students(my_connection, 'Tom', 'Soyer', 6)
    add_students(my_connection, 'Kostya', 'Dsyu', 7)

print(
    "Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
display_cities(my_connection)
while True:
    city_id = int(input("Введите ID города (или 0 для выхода): "))
    if city_id == 0:
        break
    display_students_by_city_id(my_connection, city_id)

my_connection.close()