#importing sys module for command line arguments and note functions from note.py
import sys
from db import add_note, delete_note, view_note, view_all_notes


if sys.argv[1] != "notes":
    print("Invalid command. Use 'notes' followed by a subcommand.")
    sys.exit(1)
subcommand = sys.argv[2]

#command line interface for note application
if len(sys.argv) < 2:
    print("No command provided. ")
    sys.exit(1)
command = sys.argv[1]

#command line for adding new note
if subcommand == "add":
    if len(sys.argv) < 5:
        print("Title or content missing. Use 'notes --help' for usage information.")
        sys.exit(1)
    else: 
        title = sys.argv[3]
        content = sys.argv[4] 
        note = add_note(title, content)
        print(f"Note added: {note}")
    
#command line for deleting note by id
elif subcommand == "delete":
    id = int(sys.argv[3])
    result = delete_note(id)
    print(result)

#command line for viewing note by id
elif subcommand == "show":
    id = int(sys.argv[3])
    note = view_note(id)
    if note:
        print(note)
    else:
        print(f"Note with ID {id} not found.")

#command line for viewing all notes
elif subcommand == "list":
    all_notes = view_all_notes()
    for note in all_notes:
        print(f"ID: {note[0]}")
        print(f"Title: {note[1]}")
        print(f"Content: {note[2]}")
        print("------------------")

elif subcommand == "--help":
    print("Usage:")
    print("notes add <title> <content> - Add a new note")
    print("notes delete <id> - Delete a note by ID")
    print("notes show <id> - Show a note by ID")
    print("notes list - List all notes")