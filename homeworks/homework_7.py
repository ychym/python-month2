import sqlite3

def create_table(conn):  # execute atkaruu,ishke ashyruu
    conn.execute("""DROP TABLE IF EXISTS books""")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    author TEXT,
    publication_year INTEGER,
    genre TEXT,
    number_of_pages INTEGER,
    number_of_copies INTEGER)""")

def insert_books(conn, book_id, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books
    VALUES (?,?,?,?,?,?,?)""", (book_id, name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()  # жасалган өзгөртүүлөрдү биротоло сактоо.INSERT UPDATE DELETE REPLACE mn ishtegende


def get_all_books(conn):
    result = conn.execute("""
    SELECT * FROM books""")
    return result.fetchall()

connection = sqlite3.connect('./database.db')  # database ke uloo

if __name__ == "__main__":#homework_7 = __name__ jashyruun aty.__main__ ushul file dyn maanisi
    create_table(connection)
    insert_books(connection, 1,"Сынган кылыч", "Төлөгөн Касымбеков", 1966, "Тарыхый роман", 700, 150000)
    insert_books(connection, 2, "Ак кеме", "Ч. Айтматов", 1970, "Повесть", 150, 20000)
    insert_books(connection, 3, "Курманжан Датка", "Т. Касымбеков", 1991, "Тарыхый роман", 110, 30000)
    insert_books(connection, 4, "Кылым карытар бир күн", "Ч. Айтматов", 1980, "Роман", 400, 800000)
    insert_books(connection, 5, "Маркумдар үнү", "А. Айтикеев", 1991, "Тарыхый-мемуар", 250, 10000)
    insert_books(connection, 6, "Гарри Поттер", "Ж. Роулинг", 1997-2007, "Фэнтези", 800, 6000000)
    insert_books(connection, 7, "Поллианна", "Элеанор Портер", 1913, "Классика", 250, 500000)
    insert_books(connection, 8, "Ант", "Н. Кадырбеков", 2010, "Мотивация", 200, 10000)
    insert_books(connection, 9, "Life Without Limits", "Ник Вуйчич", 2010, "Мотивация / Автобиография", 300, 100000)
    insert_books(connection, 10, "Рецепты счастья", "Э. Сафарли", 2013, "Эссе / Проза", 300, 100000)
    print(get_all_books(connection))

connection.close()
