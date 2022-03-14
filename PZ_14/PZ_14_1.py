# Из исходного текстового файла (expansion.txt) выбрать имена фалов,
# соответствующие типам: .xls, .xml, .html, .css, .py. Посчитать количество полученных
# элементов.


import re

p = re.compile(r''/[.][xhcp])


with open('expansion.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    name = len(p.findall(p, text))


print(name)


