""" Строки
Ключ, имеющий одно значение, является строкой Redis. Простые типы данных автматически преобразовываются."""



""" Подключимся к серверу Redis, раположенном на некотором хосте (по умолчанию localhost) и порте (по умолчанию 6379)"""

import redis
conn = redis.Redis()
# перечислим все ключи, которых пока нету
conn.keys('*')
# создадим простую строку (с ключем 'secret'), целое число ( с ключом 'carats'), и число с плавующей точкой (с ключом
# 'fever')
conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever', 101.5)
# получаем значения согласно заданным ключам
conn.get('secret')
conn.get('carats')
conn.get('fever')
# метод setnx() устанавливет значения, но только если ключа не существует
conn.setnx('secret', 'icky-icky-icky-ptang-boing!') # >>>False
# метод getset() возвращает старое значение и одновременно устанавливает новое
conn.getset('secret', 'icky-icky-icky-ptang-boing!') # >>> b'ni!'
conn.get('secret') # >>> b'icky-icky-icky-ptang-boing!'



