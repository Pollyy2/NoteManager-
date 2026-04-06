import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute("CREATE TABLE if not exists notes(id INTEGER PRIMARY KEY, title TEXT, content TEXT)")

con.commit()
con.close()