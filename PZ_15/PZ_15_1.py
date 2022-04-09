# Если вы видите эту надпись, значит работа не готова
from random import randint


row = int(input("Введите число строк: "))
column = int(input("Введите число столбцов: "))
matrix = []

for i in range(row):
   
   for j in range(column):
      a.append(randint(-10, 10))
   matrix.append(a)


print(matrix)


def new(matrix):
   for i in range(len(matrix)):
      for j in range(len(matrix[i])):
         if matrix[i][j] % 3 == 0:
            yield matrix[i][j] * 3


print(matrix)