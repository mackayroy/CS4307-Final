CREATE TABLE cardholders (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    genre TEXT NOT NULL,
    pages INTEGER NOT NULL,
    quality TEXT NOT NULL,
    availability INTEGER NOT NULL
);

CREATE TABLE checkouts (
    id INTEGER PRIMARY KEY,
    username INTEGER NOT NULL,
    bookId INTEGER NOT NULL,
    quality TEXT NOT NULL
);

CREATE TABLE checkins (
    id INTEGER PRIMARY KEY,
    username INTEGER NOT NULL,
    bookId INTEGER NOT NULL,
    quality TEXT NOT NULL
);
