""" Перепишем CSV-файл с помощью функции DictWriter() используя, writeheader() чтобы записать начальную строку,
содержащую имена колонок в CSV-файл"""


import csv
villiains = [
    {'first': 'No', 'last': 'Doctor'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
    ]
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villiains)