# Даны три числа.  Найти среднее из них
# (то есть число, расположенное между наименьшим и наибольшим).
a, b, c = input('введите первое число'), input('введите второе число'), input('введите третье число')

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

while c != int:
    try:
        c = int(c)
    except ValueError:
        print('введено не число')
        c = input('введите третье число')
    break

if b < a < c or c < a < b:
    print('среднее', a)
elif a < b < c or c < b < a:
    print('среднее', b)
else:
    print('среднее', c)
