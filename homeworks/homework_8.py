import sqlite3
from homework_7 import (create_table, insert_books, get_all_books)

def get_books_by_author(conn, author):
    result = conn.execute("""
    SELECT * FROM books WHERE author = ?""", (author,))
    return result.fetchall()

def delete_book_by_id(conn, book_id):
    conn.execute("""
    DELETE FROM books WHERE id = ?""", (book_id,))
    conn.commit()
    return book_id

connection = sqlite3.connect('./database.db')  # database ke uloo

print(get_books_by_author(connection,"Ж. Роулинг"))
print(f"The book is deleted, id: {delete_book_by_id(connection, 8)}.")
connection.close()
