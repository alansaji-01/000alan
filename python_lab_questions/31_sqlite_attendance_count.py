# Count present and absent students using SQL GROUP BY.
import sqlite3
records = [(1, 'Alan', 'Present'), (2, 'Anu', 'Absent'), (3, 'Arun', 'Present'), (4, 'Amal', 'Absent'), (5, 'Anna', 'Present')]
with sqlite3.connect('attendance.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS attendance (id INTEGER PRIMARY KEY, name TEXT, status TEXT)')
    cur.executemany('INSERT OR REPLACE INTO attendance VALUES (?, ?, ?)', records)
    cur.execute('SELECT status, COUNT(*) FROM attendance GROUP BY status')
    for status, count in cur.fetchall():
        print(status + ':', count)
