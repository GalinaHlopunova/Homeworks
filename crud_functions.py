import sqlite3


def initiate_db():
    connection = sqlite3.connect('not_telegram4.db')
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL
    )
    """)


def get_all_products():
    connection = sqlite3.connect('not_telegram4.db')
    cursor = connection.cursor()
    # cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    ('Обезжиренный кефир', 'Кисломолочный продукт, 30 ккал.', '100')
    # cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    ('Огурцы', 'Овощи, 15 ккал.', '200')
    # cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    ('Зеленые яблоки', 'Фрукты, 47 ккал.', '300')
    # cursor.execute(' INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
    ('Брокколи белая', 'Овощь, 34 ккал.', '400')
    products = cursor.execute('SELECT * FROM Products;')
    return products
    connection.commit()
    connection.close()


initiate_db()
get_all_products()




