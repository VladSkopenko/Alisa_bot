import sqlite3

from Decorators.Table_decorator import table_decorator


class NoteManager:
    __headers = ["Id", "Title", "Date of last update", "Note"]

    def __init__(self, db_file='Notes.db'):
        self.db_file = db_file

    def execute_query(self, query, *args):
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(query, args)
            connection.commit()

    def seed_notes(self, title, note):
        query = "INSERT INTO notes (title, note) VALUES (?, ?)"
        self.execute_query(query, title, note)

    def delete_notes_by_title(self, title):
        query = "DELETE FROM notes WHERE title=?"
        self.execute_query(query, title)

    def update_note_by_title(self, title, new_note):
        query = "UPDATE notes SET note = ? WHERE title = ?"
        self.execute_query(query, new_note, title)

    @table_decorator(__headers)
    def __str__(self):
        query = "SELECT * FROM notes"
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            notes = cursor.fetchall()
            return notes


if __name__ == "__main__":
    note_man = NoteManager()
    print(note_man)
