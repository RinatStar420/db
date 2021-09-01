
""" слудующий код записывает это стихотворение в файл 'relativity' c помощью фнукции write()"""
from poem import poem

fout = open('relativity', 'wt')
fout.write(poem)
fout.close()

