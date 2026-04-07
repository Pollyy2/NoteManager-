from db import add_note, delete_note, view_note, view_all_notes

#note manager menu for user interaction
def menu():
    print("\n===== NOTE MANAGER =====")
    print("1. Add note")
    print("2. View note by id")
    print("3. View all notes")
    print("4. Delete note")
    print("5. Exit")

#main function to run the note manager application
def main():
    while True:
        menu()
        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            note_id = add_note(title, content)
            print("Note added with id", note_id)

        elif choice == "2":
            note_id = int(input("Id: "))
            result = view_note(note_id)
            if result:
                print(result)
            else:
                print("Note not found")

        elif choice == "3":
            notes = view_all_notes()
            if notes:
                for n in notes:
                    print("\nID:", n[0])
                    print("Title:", n[1])
                    print("Content:", n[2])
                    print("------------------")
            else:
                print("No notes found")

        elif choice == "4":
            note_id = int(input("Id to delete: "))
            print(delete_note(note_id))

        elif choice == "5":
            break

        else:
            print("Invalid option")


main()
