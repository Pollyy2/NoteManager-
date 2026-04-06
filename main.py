import sys
from note import add_note, delete_note

if len(sys.argv) < 2:
    print("No command provided. ")
    sys.exit(1)
command = sys.argv[1]

if command == "add":
    id = int(sys.argv[2])
    title = sys.argv[3]
    content = sys.argv[4]
    note = add_note(id, title, content)
    print(f"Note added: {note}")

if command == "delete":
    id = int(sys.argv[2])
    result = delete_note(id)
    print(result)

