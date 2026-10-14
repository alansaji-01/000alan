# Question: Create SQLite database/table, insert three students and display all.
import sqlite3

with sqlite3.connect("college.db") as con:
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, name TEXT, course TEXT)")
    cur.executemany("INSERT OR REPLACE INTO student VALUES (?, ?, ?)", [
        (1, "Alan", "MCA"), (2, "Anu", "BCA"), (3, "Arun", "MBA")])
    cur.execute("SELECT * FROM student")
    for row in cur.fetchall():
        print(row)
