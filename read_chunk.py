"""
Можно указать максимальное количечтво символов, которое функция read() вернет за один вызов. Считаем 100 симвлов
за раз и присоеденим каждный врагмент к строке poem, чтобы воссоздать оригинал.
"""

poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
        fragment = fin.read(chunk)
        if not fragment:
            break
        poem += fragment

fin.close()
print(poem)
print('\n',len(poem))