import math
standart_radius = 5
__all__ = ['circle_perimetr', 'circle_area']


def circle_perimetr(radius=standart_radius):
    return 2 * math.pi * radius


def circle_area(radius=standart_radius):
    return math.pi * radius ** 2