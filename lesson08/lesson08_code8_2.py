import sqlite3

with sqlite3.connect('C:\\Users\\0104_Python\\Desktop\\SQLite_lesson\\sample.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM EMPLOYEE')
    for row in cursor.fetchall():
        print(row[0], end='')
        print(row[1], end='')
        print(row[2], end='')
        print(row[3], end='')
        print(row[4], end='')
        print(row[5], end='')
        print()