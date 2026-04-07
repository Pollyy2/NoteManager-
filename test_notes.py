from db import add_note, delete_note, view_note

note_id = ""

def test_add_note():
    global note_id
    note_id = add_note("Test Note", "This is a test note.")
    assert isinstance(note_id, int)
    return note_id

def test_delete_note():
    global note_id
    delete_note(note_id)
    note = view_note(note_id)
    assert note is None

test_add_note()
test_delete_note()