import sqlite3


def create_db():
    with open('Note_db_model.sql', 'r') as f:
        sql = f.read()
    with sqlite3.connect('Notes.db') as con:
        cur = con.cursor()
        cur.executescript(sql)
