"""
Чтение бинарных файлов с помощью функции read()  выглядит проще простого, всё,что нам нужно - открыть файл в режиме 'rb'
"""

fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)
fin.close()
print(bdata)