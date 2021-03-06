""" Форматф dbm представляют собой хранилища, работающие по принципу 'ключ-значение', их часто встраивают в приложения
вроде браузеров. База dbm очень похожа на обычный словарь.
- Присваивание значения ключу, и оно автоматически сохраняется в бд на диске
- Можем получить значение с помощью клуча
Напишу пример. Второй аргумент метода open() может принимать значение 'r', 'w', 'c'(чтение и запись), создовая файл,
если он отсутствует."""

import dbm

db = dbm.open('definitions', 'c')
# Для создания пары ключ-значение просто присвоим знасение ключу (как в словаре)
db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'
print(len(db))
print(db['pesto'])
db.close()