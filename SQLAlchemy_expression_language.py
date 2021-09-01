""" Второй уровень SQLAlchemy - язык выражений SQL.
Он предоставляет функции, которые позволяютс создать SQL для разных операций. Язык выражений обрабатывает большее
кол-во различий диалектов, чем низкоуровневый слой движка."""

import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
# Для определении таблицы zoo вместо SQL используем язык выражений
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float)
               )
meta.create_all(conn)
# Запись в таблицу данные с помощью новых функций языка выражений
conn.execute(zoo.insert(('bear', 2, 1000.00)))
conn.execute(zoo.insert(('weasel', 1, 2000.00)))
conn.execute(zoo.insert(('duck', 10, 0)))
# Далее создам оператор SELECT (zoo.select() делает выборку всего, что содержится в таблице
result = conn.execute(zoo.select())
# Получим результат
rows = result.fetchall()
print(rows)