# Дано число R и список размера N. Найти два различных элемента списка, сумма
# которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания их
# индексов (определение наиболее близких чисел - то есть такой элемент AK, для
# которого величина |AK - R| является минимальной).

from random import randint
razmer = int(input('введите размер списка'))
r = int(input('введите r'))
a = []
sum = 0
min_1 = 0
min_2 = 0
value = 0
b = 1000


for i in range(razmer):  # заполнение списка
    a.append(randint(0, 100))
print(a)
a.append(0)


for i in range(len(a) - 1):
    sum = a[i] + a[i + 1]
    value = abs(r - sum)
    if value < b:
        b = value
        min_1 = a[i]
        min_2 = a[i + 1]
print('первый индеккс', min_1)
print('второй индекс', min_2)
