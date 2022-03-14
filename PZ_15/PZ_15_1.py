# В матрице элементы кратные 3 увеличить в 3 раза.

massiv_start = [[1, 2, 3, 6, 8, 9], [12, 6, 14, 15, 21, 5]]


massiv_end = [n * 3 for n in massiv_start if (n%3==0) ]


print(massiv_end)