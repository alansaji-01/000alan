# Insert products in SQLite and display products priced above 500.
import sqlite3
products = [(1, 'Keyboard', 800), (2, 'Pen', 20), (3, 'Mouse', 600), (4, 'Notebook', 100), (5, 'Monitor', 8000)]
with sqlite3.connect('shop.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
    cur.executemany('INSERT OR REPLACE INTO product VALUES (?, ?, ?)', products)
    cur.execute('SELECT * FROM product WHERE price > ?', (500,))
    for row in cur.fetchall():
        print(row)
