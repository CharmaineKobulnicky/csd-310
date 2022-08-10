""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode


""" database config object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host" : "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}


def show_menu():
    print("\n -- Main Menu --")

    print("     1. View Books\n     2. View Store Location\n    3. My Account\n     4. Exit Program")

    try:
        choice = int(input('        <Example enter: 1 for book listing>: '))

        return choice
    except ValueError:
        print("\n  Invalid number, program terminated...\n")

        sys.exit(0)

def show_books(_cursor):
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    # cursor object result
books = _cursor.fetchall()

