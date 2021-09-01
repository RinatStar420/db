""" Создади bd enterprise.db и таблицу zoo (контакный зоопарк) для управления нашим бизнесом по содержание
придорожного зоопарка. В таблице будут содержаться следующие графы:
 critter - строка переменной длинный, наш первичный ключ
 count - целочисленное значение едениц используемого инвентаря для этого животного
 damages - кол-во баксов, потерянных из-за взаимодействия людей с животными"""

import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
# curs.execute('''CREATE TABLE zoo
# (critter VARCHAR(20) PRIMARY KEY,
#  count INT,
#  damage FLOAT)''')
#
# # Добавим в зоопарк несколько животых
#
curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')


""" Существует способ более безопаснее добавить данные - через заполнитель"""
ins = 'INSERT INTO zoo (critter, count, damage) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))

# Теперь проверим сможем ли получить назад список животных

curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

# Получаем упорядоченный список по колву животных

curs.execute('SELECT * FROM zoo ORDER BY count')
rows = curs.fetchall()
print(rows)

# Получаем в нисходящем порядке

curs.execute('SELECT * FROM zoo ORDER BY count DESC')
rows = curs.fetchall()
print(rows)


# Какие животные обходятся дороже всего

curs.execute('''SELECT * FROM zoo WHERE damage = (SELECT MAX(damage) FROM zoo)''')
rows = curs.fetchall()
print(rows)


# После работы с бд нам необходимо закрыть соединени(connect) и курсок(cursor)

curs.close()
conn.close()