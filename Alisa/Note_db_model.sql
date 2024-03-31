-- Table: notes
DROP TABLE IF EXISTS notes;
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    title VARCHAR(35) UNIQUE NOT NULL,
    date_of_update DATE DEFAULT CURRENT_DATE,
    note TEXT
    com
);