#В матрице найти среднее арифметическое элементов последних двух столбцов.

import numpy as np

a = np.array([[1, 2, 3], [4, 6, 8], [2, 5, 6]])
print('Начальная матрица:')


for i in a:
    print(*i)
    
    
print('Среднее арифметическое элементов последних двух столбцов: ')
print(sum(a[:, -1] + a[:, -2]) / (len(a[:, -1]) + len(a[:, -2]))) 

