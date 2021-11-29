# Дан список размера N, все элементы которого, кроме первого, упорядочены по
# возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
# позицию.


data_list = [6, 1, 2, 3, 4, 5, 7, 8, 9]
print(data_list)
elem = data_list.pop(0)
nev = []
i = 1


for i, x in enumerate(data_list):  # получаем индек и значение элементов списка
    if data_list[i] > elem:
        nev.append(elem)
        break
    nev.append(x)


nev = nev + data_list[i::]
print(nev)
