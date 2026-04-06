from db import add_note, delete_note, view_note

def test_add_note():
    note_id = add_note("Test Note", "This is a test note.")
    assert isinstance(note_id, int)
    print(f"Note added with ID: {note_id}")

def test_delete_note():
    note_id = add_note("Note to Delete", "This note will be deleted.")
    result = delete_note(note_id)
    assert result == f"Note {note_id} deleted."
    print(result)

test_add_note()
test_delete_note()