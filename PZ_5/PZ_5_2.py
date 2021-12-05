# Описать функцию PowerA234(A, B, C, D), вычисляющую вторую, третью и четвертую
# степень числа A и возвращающую эти степени соответственно в переменные B, C и D (A —
# входной, B, C, D — выходные параметры; все параметры являются вещественными).
# С помощью этой функции найти вторую, третью и четвертую степень пяти данных чисел.


def powera234(a):
    l_step1 = pow(a, 1)
    l_step2 = pow(a, 2)
    l_step3 = pow(a, 3)
    l_step4 = pow(a, 4)
    return l_step1, l_step2, l_step3, l_step4


for i in range(5):
    s = float(input('введите входное число = '))
    step1, step2, step3, step4 = float(s), float(s), float(s), float(s)
    g_step1, g_step2, g_step3, g_step4 = powera234(step1)
    print('вторая степень числа = ',g_step2 )
    print('третья степень числа = ',g_step3 )
    print('четвёртая степень числа = ',g_step4 )
