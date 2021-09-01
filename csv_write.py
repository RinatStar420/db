""" Запись csv файла"""
import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Lebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
]
with open('villains', 'wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)


