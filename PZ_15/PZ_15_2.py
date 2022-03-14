# В матрице найти среднее арифметическое элементов последних двух столбцов.
from functools import reduce
import numpy


massiv_start = [[1, 2, 3, 6, 8, 9], [12, 6, 14, 15, 21, 5]]


lst_len = len(massiv_start)
lst_avg = numpy.average(massiv_start)

print(lst_avg)

