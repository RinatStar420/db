""" В самом верхнем слое SQLAlchemy объектно-реляционное отображение (ORM) использует язык выражений SQL, но
старается сделать реальные механизмы базы данных невидимыми. Мы определяем классы, а ОРМ обрабатывает способ, с
помощью которого они получают данные из базы данных и возвращают их обратно.
Мы определим класс Zoo и свяжем его с ОРМ. В этот раз укажем SQL использовать файд zoo.db, чтобы убедиться, что
ОРМ работает"""

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

# Вот так создается соединение
conn = sa.create_engine('sqlite:///zoo.db')
# Теперь начнём работу с SQLAlchemy ORM. Определяем класс Zoo и связываем его атрибуты
# с графами таблицы
Base = declarative_base()


class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)

    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages

    def __repr__(self):
        return "<Zoo({},{},{})>".format(self.critter, self.count, self.damages)


# Следующая строка создает бызу данных и таблицу
Base.metadata.create_all(conn)
# добавлю в таблицу данные путем создания объектов Python. ORM управляет данными из нутри
first = Zoo('duck', 10, 0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)

# Создание сессии для беседы с базой данных
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=conn)
session = Session()
# Внутри сессии записываем три созданных объекта в базу данных. Функция add() добавляет один объект
# а функция add_all() добавляет список
session.add(first)
session.add_all([second, third])
# Завершаем сессию
session.commit()
