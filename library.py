
import sqlite3
from datetime import datetime
import argparse
import random
from faker import Faker
from data import getBooks, getUsernames

conn = sqlite3.connect('libraryDB.db')
cursor = conn.cursor()

def bookSetUp():
    books = getBooks()
    conditionOfBook = ["Good", "Very Good", "Poor", "Fair"]
    for book in books:
        condition = random.choice(conditionOfBook)
        cursor.execute("INSERT INTO books (name,genre,pages,quality, availability) VALUES (?,?,?,?,?)", (book["title"],book["genre"].split(",")[0],book["page_count"],condition, 1))
        conn.commit()

def checkOutSetup():
    cursor.execute("SELECT id FROM cardholders")
    cardholderID = cursor.fetchall()
    cursor.execute("SELECT id FROM books WHERE availability = 1")
    bookID = cursor.fetchall()  


    for _ in range(100):
        insetCard = random.choice(cardholderID)[0]
        cursor.execute("SELECT name from cardholders WHERE id = ?", (insetCard,))
        name = cursor.fetchone()
        insertBook = random.choice(bookID)[0]
        cursor.execute("SELECT name from books WHERE id = ?", (insertBook,))
        book = cursor.fetchone()
        cursor.execute("SELECT quality FROM books WHERE id = ?", (insertBook,))
        quality = cursor.fetchone()
        insertQuality = quality[0]
        cursor.execute("INSERT INTO checkouts (cardholderId, bookId, quality) VALUES (?,?,?)", (insetCard,insertBook,insertQuality))
        cursor.execute("UPDATE books SET availability = 0 WHERE id = ?", (insertBook,))
        print(f"{name[0]} checkout the book {book[0]} today.")
    conn.commit()

def populate():
    bookSetUp()
    usernames = getUsernames()
    fake = Faker()
    names = [fake.name() for _ in range(100)]
    for i in range(100):
        cursor.execute("INSERT INTO cardholders (name, username) VALUES (?,?)", (names[i], usernames[i]))
        conn.commit()
    checkOutSetup()

def getAvailableBooks():
    cursor.execute("SELECT * FROM books WHERE availability = 1")
    books = cursor.fetchall()
    for book in books:
        print("Available Books")
        print("----------------")
        print(book[1])
    conn.commit()

def getAvgPages():
    cursor.execute("""SELECT genre, AVG(pages) FROM books GROUP BY genre""")
    books = cursor.fetchall()
    for book in books:
        print(f"The Genre {book[0]} has the average page count of {round(book[1],0)}")

def cardHolderBooks(username):
    cursor.execute("""SELECT books.name FROM books 
                   JOIN checkouts ON books.id = checkouts.bookId
                   JOIN cardholders ON checkouts.cardholderId = cardholders.id
                   WHERE cardholders.username = ?""",(username,))

    userbooks = cursor.fetchall()
    for book in userbooks:
        print(f"{username} has checkout {book[0]}")

def addCardholder(name, username):
    print(f"User with the name {name} created a username {username}")
    cursor.execute("INSERT INTO cardholders (name, username) VALUES (?,?)", (name, username))
    conn.commit()

def addBook(name, genre, pages, quality, availability):
    print(f"{name} was added into the library")
    cursor.execute("INSERT INTO books (name, genre, pages, quality, availability) VALUES (?,?,?,?,?)", (name, genre, pages, quality, availability))
    conn.commit()

def checkOutBook(cardholderId, bookId, quality):
    print(f"Book was checkout")
    cursor.execute("INSERT INTO checkouts (cardholderId, bookId, quality) VALUES (?,?,?)", (cardholderId, bookId, quality))
    cursor.execute("UPDATE books SET availability = 0 WHERE id = ?", (bookId,))
    conn.commit()

def returnBook(cardholderId, bookId):
    print(f"Book was returned")
    cursor.execute("DELETE FROM checkouts WHERE cardholderId = ? AND bookId = ?", (cardholderId, bookId))
    cursor.execute("UPDATE books SET availability = 1 WHERE id = ?", (bookId,))
    conn.commit()

def main():
    parser = argparse.ArgumentParser(description='Simple social network CLI')
    parser.add_argument('action', choices=['populate','getBooks','mostAvailablePopular', 'addCardholder', 'addBook', 
                                           'checkOutBook', 'returnBook','getAvgPages','cardHolderBooks'],
                        help='Action to perform')
    
    parser.add_argument('--name')
    parser.add_argument('--username')
    parser.add_argument('--genre')
    parser.add_argument('--pages')
    parser.add_argument('--quality')
    parser.add_argument('--availability')
    parser.add_argument('--cardholderId')
    parser.add_argument('--bookId')

    args = parser.parse_args()
    
    if args.action == 'populate':
        populate()
    if args.action == 'getAvailableBooks':
        getAvailableBooks()
    if args.action == 'getAvgPages':
        getAvgPages()
    if args.action == 'addCardholder':
        addCardholder(args.name, args.username)
    if args.action == 'addBook':
        addBook(args.name, args.genre, args.pages, args.quality, args.availability)
    if args.action == 'checkOutBook':
        checkOutBook(args.cardholderId, args.bookId, args.quality)
    if args.action == 'returnBook':
        returnBook(args.cardholderId, args.bookId)
    if args.action == 'cardHolderBooks':
        cardHolderBooks(args.username)
    

if __name__ == "__main__":
    main()

conn.close()