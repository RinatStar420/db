""" На уровне движка возможности почти не отличаются от функций DB-API.
Работы буут производиться с SQLite, поскольку поодержка уже встроена в Питон.
Строка соединения для SQLite опускает значения параметров host, port, user и password.
dbname информирует SQLite о том, какой файл использовать для хранений моей базы данных"""

import sqlalchemy as sa
# Соединение с бд и создание хранилища в памяти
""" Простое изменение строки соединения позволит перенести этот код на базу данных другого типа"""
conn = sa.create_engine('sqlite://')
# Создание таблици с названием zoo и содержанием трёх граф
conn.execute('''CREATE TABLE zoo
 (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
""" Вызов conn.execute возвращает объект SQLAlchemy, который называется ResultProxy"""
# Вставка трёх наборов данных в новую пустую таблицу
ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)
# Создание выборки того, что только что разместил в базе
rows = conn.execute('SELECT * FROM zoo')
# в SQLAlchemy rows не является списком - это специальный объект ResultProxy, который мы не может
# непосредственно отобразить
# однако его можно проитерировать, как список, и получить по одному ряду за раз
for row in rows:
    print(row)
