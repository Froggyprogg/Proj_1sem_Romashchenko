# Даны целые положительные числа A и B (A > B).
# Вывести все целые числа от A и B включительно;
# При этом каждое число должно выводиться столько раз, каково его значение.


a, b = input('введите первое число: '), input('введите второе число: ')

while a != int:  # проверка исключений
    try:
        a = int(a)
    except ValueError:
        print('введено не число')
        a = input('введите первое число')
    break

while b != int:
    try:
        b = int(b)
    except ValueError:
        print('введено не число')
        b = input('введите второе число')
    break

while a <= b:
    print(str(a) * a)
    a += 1
