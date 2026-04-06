#Note object with id, title, content
class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        

    def __str__(self):
        return f"ID: {self.id}\nTitle: {self.title}\nContent: {self.content}"

#empty list to store notes 
notes = []
#function to add notes 
def add_note(title, content):
    id = len(notes) + 1
    new_note = Note(id, title, content)
    notes.append(new_note)
    return new_note

#function to delete note by id
def delete_note(id):
    for n in notes:
        if n.id == id:
            notes.remove(n)
            return f"Note {id} deleted."

#function to view note by id 
def view_note(id):
    for n in notes:
        if n.id == id:
            return n 

#function to view all notes iterates through notes list and prints each note
def view_all_notes():
    for n in notes:
        print("------------------")
        print(n)


              
