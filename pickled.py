""" Сериализация структуры данных дата/время"""

import pickle
import datetime

now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)

print(now1)
print(pickled)
print(now2)
