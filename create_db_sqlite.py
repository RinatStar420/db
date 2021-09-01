import csv
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()

with open('books1','rt') as fin:
    # csv.DictReader по умолчанию использует первую строку в файле для заголовков столбцов
    dr = csv.DictReader(fin)
    to_db = [(i['title'], i['author'], i['year']) for i in dr]

curs.executemany("INSERT INTO books (title, author, year ) VALUES (?, ?, ?);", to_db)
curs.fetchall()


curs.execute('SELECT * FROM books')
print(curs.fetchall())

curs.close()
conn.close()




