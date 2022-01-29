# Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке


k = 0
for i in open('text18-18.txt', encoding='utf-8'):
    print(i, end='')
    for z in i:
        if z == ',':
            k += 1
        if z == ',':
            k += 1
        if z == '.':
            k += 1
        if z == '-':
            k += 1
        if z == '-':
            k += 1
print()
print('количество знаков =', k, )


file = open('text18-18.txt', 'r', encoding='utf-8')
s = file.readlines()
s.reverse()
file.close()


file = open('text18-18_new.txt', 'w', encoding='utf-8')
file.write(''.join(s))