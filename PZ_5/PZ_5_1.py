# Составить программу, в которой функция генерирует четырехзначное число и определяет,
# есть ли в числе одинаковые цифры.


from random import randint


def generator(m):
    m = randint(1000, 9999)
    print(m)
    a = (m // 1000) % 10
    b = (m // 100) % 10
    c = (m // 10) % 10
    d = m % 10
    return a, b, c, d


vxod = 1
g_1, g_2, g_3, g_4 = generator(vxod)
if (g_1 == g_2) or (g_1 == g_3) or (g_1 == g_4) or (g_2 == g_3) or (g_2 == g_4) or (g_4 == g_3):
    print('есть одинаковые')
else:
    print('нет одинаковых')
