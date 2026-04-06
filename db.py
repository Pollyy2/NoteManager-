import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()
#create notes table with id, title and content
cur.execute("CREATE TABLE if not exists notes(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)")

#function to add note to database 
def add_note(title, content):
    cur.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    con.commit()
    return cur.lastrowid

#function to delete note by id from database
def delete_note(id):
    cur.execute("DELETE FROM notes WHERE id = ?", (id,))
    con.commit()
    return f"Note {id} deleted."

#function to view note by id from database
def view_note(id):
    cur.execute("SELECT * FROM notes WHERE id = ?", (id,))
    note = cur.fetchone()
    if note:
        return f"ID: {note[0]}\nTitle: {note[1]}\nContent: {note[2]}"
    else:
        return None
    
#function to view all notes from database 
def view_all_notes():
    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()
    con.close()
    return notes


