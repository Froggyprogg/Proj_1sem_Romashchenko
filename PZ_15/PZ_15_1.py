# В матрице элементы кратные трём увеличить в 3 раза

from random import randint 


n, m = [int(input(i)) for i in ('Введите кол-во столбцов: ', 'Введите кол-во строк:')]
matr = [[random.randint(1, 6) for j in range(n)] for i in range(m)]


print('Начальная матрица: ')
for i in matr:
    print(*i)


print('Измененная матрица: ')
izm = lambda x: x % 3 == 0
for i in matr:                                          
    for j in i:
        if izm(j):
            j *= 3
        print(j, end=' ')
    print() 
