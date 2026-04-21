# from lessons.lesson_4_2 import Playlist
from lessons.database import (
    create_table,
    add_student, get_all_students)
import sqlite3

# play = Playlist("playlist")
# print(play)
connection = sqlite3.connect('database.db')
create_table(connection)
add_student(connection, "Ai", 27, "Bishkek")
add_student(connection, "Nur", 18, "Osh")
print(get_all_students(connection))
connection.close()
