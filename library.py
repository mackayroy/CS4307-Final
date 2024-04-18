
import sqlite3
from datetime import datetime
import argparse
import random

conn = sqlite3.connect('libraryDB.db')
cursor = conn.cursor()

def populate():
    pass


def create_user(name):
    print(f"User created with the name {name}")
    cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()


def main():
    parser = argparse.ArgumentParser(description='Simple social network CLI')
    parser.add_argument('action', choices=['populate'],
                        help='Action to perform')
    
    parser.add_argument('--name')
    

    args = parser.parse_args()
    
    if args.action == 'create_user':
        create_user(args.name)
    
    

if __name__ == "__main__":
    main()

conn.close()