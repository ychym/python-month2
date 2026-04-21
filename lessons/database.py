import sqlite3

def create_table(conn):#execute atkaruu,ishke ashyruu
    conn.execute("""DROP TABLE IF EXISTS students""")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    city TEXT
    )
    """)

def add_student(conn, name, age, city):
    conn.execute("""
    INSERT INTO students
    VALUES (?, ?, ?)""", (name, age, city))
    conn.commit()

def get_all_students(conn):
    result = conn.execute("""
    SELECT * FROM students""")
    return result.fetchall()#fetch serverden maalymatty aluu.тизме (list) кайтарат. Ал тизменин ичиндеги ар бир катар кортеж (tuple) түрүндө болот.

def get_one_student(conn, student_id):
    ...



def delete_student(conn, student_id):
    conn.execute("""
    DELETE * FROM students WHERE id = ?""", (student_id,))
    conn.commit()