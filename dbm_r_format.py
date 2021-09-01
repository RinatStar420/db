"""Чтении файла формата dbm"""

import dbm
db = dbm.open('definitions', 'r')
print(db['ketchup'])