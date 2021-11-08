# Дано вещественное число X и целое число N (> 0).
# Найти значение выражения 1 + X + X^2 / (2!) + ... + X^N / (N!) (N! = 1*2 ...N).
# Полученное число является приближенным значением функции exp в точке X.


x, n = input('введите первое число'), input('введите второе число')

while x != float:  # проверка исключений
    try:
        x = float(x)
    except ValueError:
        print('введено не число')
        x = input('введите первое число')
    break

while n != int:  # проверка исключений
    try:
        n = int(n)
    except ValueError:
        print('введено не число')
        n = input('введите второе число')
    break

fact = 1
i = 1
summa = 1
stepen = 1
while n > 0 :
    stepen = stepen * x
    fact = fact * i
    i += 1
    summa = summa + stepen/fact
    n -= 1
print('значение функции exp в точке x = ', summa)
