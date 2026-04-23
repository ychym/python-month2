# from lessons.lesson_4_2 import Playlist
import sqlite3
from lessons.database import (
    create_table,
    add_student, get_all_students)

# play = Playlist("playlist")
# print(play)
connection = sqlite3.connect('database.db')
create_table(connection)
add_student(connection, 1, "Ai", 27, "Bishkek")
add_student(connection, 2, "Nur", 18, "Osh")
print(get_all_students(connection))
connection.close()

#print("==delete==")
#delete_student(connection, 1)
