# Insert monthly expenses into SQLite and calculate their total using SUM().
import sqlite3
expenses = [(1, 'January', 5000), (2, 'February', 4500), (3, 'March', 6000)]
with sqlite3.connect('expenses.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, month TEXT, amount REAL)')
    cur.executemany('INSERT OR REPLACE INTO expenses VALUES (?, ?, ?)', expenses)
    cur.execute('SELECT SUM(amount) FROM expenses')
    print('Total expenses:', cur.fetchone()[0] or 0)
