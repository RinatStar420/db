""" Pickle также работает с нашими собственными классами и объектами. Определим небольшой класс, который
называется Tiny  и возвращает слово 'tiny', когда он используется как строка"""

import pickle


class Tiny():
    def __str__(self):
        return 'tiny'


obj1 = Tiny()

pickled = pickle.dumps(obj1)

obj2 = pickle.loads(pickled)

print(type(obj2))

print(pickled)
print(type(obj1))
print(str(obj1))
