# Дано трёхзначное число.
# В нём зачеркнули первую слева цифру и приписали её слева.
# Вывести.
try:  # Проверка исключений
    a = int(input('Введите число:'))
    b = a // 100
    c = a % 100
    s = (c * 10) + b
    print(s)
except ValueError:
    print('Введено не число')
