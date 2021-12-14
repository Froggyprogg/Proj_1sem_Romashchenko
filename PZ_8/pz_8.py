# Дан словарь на 6 персон, найти и вывести наибольшее и наименьшее
# значение роста (в см.). (Пример, {"Андрей": 178, "Виктор": 150, "Максим": 200, …},
# наибольшее 200, наименьшее 150)]


from random import randint

start_dict = dict()

# далее заполняю список значениями
start_dict['Антон'] = randint(150, 200)
start_dict['Матвей'] = randint(150, 200)
start_dict['Егор'] = randint(150, 200)
start_dict['Денис'] = randint(150, 200)
start_dict['Николай'] = randint(150, 200)
start_dict['Максим'] = randint(150, 200)
print(start_dict)

# поиск наибольшего и наименьшего из значений
max_value = max(start_dict.values())
min_value = min(start_dict.values())


print('наибольшее значение роста: ', max_value)
print('наименьшее значение роста: ', min_value)
