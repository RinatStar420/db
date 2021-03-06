"""
Если не закрыть файл за собой, его закроет Питон после того, как будет удалена последняя ссылка на него. Это значит,
что, если открыть файл и не закрыть его явно, он будет закрыть автоматически по завершению функции. ( Но мы можем открыть
файл внутри длинной функции или даже основного раздела программы). Файл должен быть закрыть, чтобы все оставшиеся оперции
записи были завершены.

Используем консрукцию   with выражение as переменная
"""
from poem import poem

with open('relativity', 'wt') as fout:
    fout.write(poem)