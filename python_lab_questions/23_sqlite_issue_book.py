# Create library table and issue a book by changing available to No.
import sqlite3
with sqlite3.connect('library.db') as con:
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, available TEXT)')
    cur.execute('INSERT OR IGNORE INTO books VALUES (?, ?, ?)', (1, 'Python', 'Yes'))
    book_id = int(input('Enter book ID: '))
    cur.execute("UPDATE books SET available = 'No' WHERE id = ? AND available = 'Yes'", (book_id,))
    print('Book issued successfully' if cur.rowcount else 'Book unavailable or invalid ID')
    cur.execute('SELECT * FROM books')
    for row in cur.fetchall():
        print(row)
