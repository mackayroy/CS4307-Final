rm -f libraryDB.db
sqlite3 libraryDB.db < schema.sql

python3 library.py populate