import sys
from note import add_note, delete_note, view_note, notes, view_all_notes

if len(sys.argv) < 2:
    print("No command provided. ")
    sys.exit(1)
command = sys.argv[1]

if command == "add":
    title = sys.argv[2]
    content = sys.argv[3]
    note = add_note(title, content)
    print(f"Note added: {note}")
    

if command == "delete":
    id = int(sys.argv[2])
    result = delete_note(id)
    print(result)

if command == "view":
    id = int(sys.argv[2])
    note = view_note(id)
    if note:
        print(note)
    else:
        print(f"Note with ID {id} not found.")

if command == "view_all":
    all_notes = view_all_notes()
    for note in all_notes:
        print(note)
