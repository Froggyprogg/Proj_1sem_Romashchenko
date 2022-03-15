# Из исходного текстового файла (expansion.txt) выбрать имена фалов,
# соответствующие типам: .xls, .xml, .html, .css, .py. Посчитать количество полученных
# элементов.


import re
pattern = re.compile(r"[.](xls|xml|html|css|py)")


with open('expansion.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    number = list(re.findall(pattern, text))


print("Количество элементов = ", len(number))