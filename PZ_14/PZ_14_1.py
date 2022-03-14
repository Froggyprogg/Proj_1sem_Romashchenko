# Из исходного текстового файла (expansion.txt) выбрать имена фалов,
# соответствующие типам: .xls, .xml, .html, .css, .py. Посчитать количество полученных
# элементов.


import re

p = re.compile(r'[.])
with open('expansion.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    name = (p.findall)

