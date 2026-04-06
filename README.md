# Note Manager CLI

## Description

A simple command-line application for creating and managing notes using Python and SQLite.

## How to run

Run the application from the terminal:

```bash
./notes <command>
```

Or:

```bash
python main.py notes <command>
```

## Commands

```bash
notes add "Title" "Content"      # create a new note
notes list                       # show all notes
notes show <id>                  # show note by id
notes delete <id>                # delete note by id
notes --help                     # show usage
```

## Note Structure

Each note contains:

* id (auto-incremented integer)
* title (required)
* content

## Storage

Notes are stored locally in a SQLite database (`database.db`).

## Project Structure

* main.py – handles command-line interaction
* db.py – contains business logic and database operations

## Testing

Basic test cases are implemented in `test_notes.py`.

Run tests with:

```bash
python test_notes.py
```
