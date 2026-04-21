import sqlite3

def create_table(conn):  # execute atkaruu,ishke ashyruu
    conn.execute("""DROP TABLE IF EXISTS books""")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books(
    name TEXT NOT NULL,
    author TEXT,
    publication_year INTEGER,
    genre TEXT,
    number_of_pages INTEGER,
    number_of_copies INTEGER)""")


def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books
    VALUES (?,?,?,?,?,?)""", (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()  # жасалган өзгөртүүлөрдү биротоло сактоо.INSERT UPDATE DELETE REPLACE mn ishtegende


def get_all_books(conn):
    result = conn.execute("""
    SELECT * FROM books""")
    return result.fetchall()

connection = sqlite3.connect('./database.db')  # database ke uloo

if __name__ == "__main__":#homework_7 = __name__ jashyruun aty.__main__ ushul file dyn maanisi
    create_table(connection)
    insert_books(connection, "Ant", "N.K.", 2018, "novel", 500, 200)
    insert_books(connection, "AK keme", "Ch.A.", 1990, "novel", 3000, 200)
    insert_books(connection, "A", "N.K.", 1850, "novel", 1000, 300)
    insert_books(connection, "B", "N.K.", 2000, "novel", 300, 200)
    insert_books(connection, "C", "N.K.", 2026, "novel", 400, 100)
    insert_books(connection, "D", "N.K.", 2018, "novel", 2000, 20)
    insert_books(connection, "E", "N.K.", 2018, "novel", 500, 200)
    insert_books(connection, "F", "Ch.A.", 1990, "novel", 3000, 200)
    insert_books(connection, "G", "N.K.", 1850, "novel", 1000, 300)
    insert_books(connection, "H", "N.K.", 2000, "novel", 300, 200)
    print(get_all_books(connection))

connection.close()
