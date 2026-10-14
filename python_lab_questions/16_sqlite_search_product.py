# Search for a product by name in SQLite and handle a missing result.
import sqlite3
with sqlite3.connect('shop.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
    cur.executemany('INSERT OR IGNORE INTO product VALUES (?, ?, ?)', [(1, 'Keyboard', 800), (2, 'Pen', 20), (3, 'Mouse', 600), (4, 'Notebook', 100), (5, 'Monitor', 8000)])
    name = input('Enter product name: ').strip()
    cur.execute('SELECT * FROM product WHERE name = ? COLLATE NOCASE', (name,))
    row = cur.fetchone()
    print(row if row else 'Product not found')
