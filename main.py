import sqlite3

db = sqlite3.connect("coffee.db")
cursor = db.cursor()

request = cursor.execute("SELECT * FROM coffee").fetchall()
for _ in request:
    print(_)