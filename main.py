#importing sys module for command line arguments and note functions from note.py
import sys
from db import add_note, delete_note, view_note, view_all_notes

#command line interface for note application
if len(sys.argv) < 2:
    print("No command provided. ")
    sys.exit(1)
command = sys.argv[1]

#command line for adding new note
if command == "add":
    title = sys.argv[2]
    content = sys.argv[3]
    note = add_note(title, content)
    print(f"Note added: {note}")
    
#command line for deleting note by id
if command == "delete":
    id = int(sys.argv[2])
    result = delete_note(id)
    print(result)

#command line for viewing note by id
if command == "view":
    id = int(sys.argv[2])
    note = view_note(id)
    if note:
        print(note)
    else:
        print(f"Note with ID {id} not found.")

#command line for viewing all notes
if command == "view_all":
    all_notes = view_all_notes()
    for note in all_notes:
        print(f"ID: {note[0]}")
        print(f"Title: {note[1]}")
        print(f"Content: {note[2]}")
        print("------------------")
 