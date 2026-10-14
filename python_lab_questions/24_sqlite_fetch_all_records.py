# Insert sample course records and fetch all records using a loop.
import sqlite3
with sqlite3.connect('course.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS course (id INTEGER PRIMARY KEY, name TEXT)')
    cur.executemany('INSERT OR REPLACE INTO course VALUES (?, ?)', [(1, 'MCA'), (2, 'BCA'), (3, 'MBA')])
    cur.execute('SELECT * FROM course')
    for row in cur:
        print(row)
