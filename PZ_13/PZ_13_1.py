# В последовательности на n целых элементов найти произведение элементов средней трети.
from random import randint

n = input("Введите количество элементов последовательности = ")
i = 0


posled_start = []
for i in range(int(n)):
    posled_start.append(randint(0, 100))
print(posled_start)

for a in posled_start:
    b = int((n[a])) + int((n[a+1]))
print(posled_start)
