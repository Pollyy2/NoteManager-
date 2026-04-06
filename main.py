import sys
from note import add_note

if len(sys.argv) < 2:
    print("No command provided. ")
    sys.exit(1)
command = sys.argv[1]

if command == "add":
    title = sys.argv[2]
    content = sys.argv[3]
    note = add_note(1,title, content)
    print(f"Note added: {note}")

