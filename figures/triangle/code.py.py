import math
__all__ = ['triangle_area', 'triangle_perimetr']
a_d = 7
b_d = 2
c_d = 8


def triangle_perimetr(a=a_d, b=b_d, c=c_d):
    return a + b + c


def triangle_area(a=a_d, b=b_d, c=c_d):
    p = a + b + c
    return math.sqrt(p * (p - a) * (p - b) * (p - c))