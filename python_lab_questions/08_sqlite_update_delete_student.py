# Question: Update a student's course and delete a record using SQLite.
import sqlite3

with sqlite3.connect("college.db") as con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name TEXT, course TEXT)")
    cur.executemany("INSERT OR IGNORE INTO student VALUES (?, ?, ?)", [(1, "Alan", "MCA"), (2, "Anu", "BCA"), (3, "Arun", "MBA")])
    cur.execute("UPDATE student SET course = ? WHERE id = ?", ("MCA", 2))
    cur.execute("DELETE FROM student WHERE id = ?", (3,))
    cur.execute("SELECT * FROM student")
    for row in cur.fetchall():
        print(row)
