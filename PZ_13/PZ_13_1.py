# В последовательности на n целых элементов найти произведение элементов средней трети.
from random import randint

n = int(input("Введите количество элементов последовательности = "))
i = 0
posled_start = []
for i in range(n):  # заполнение списка
    posled_start.append(randint(0, 100))
print(posled_start)


