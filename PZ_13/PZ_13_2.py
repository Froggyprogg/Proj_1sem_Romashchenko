# Составить генератор (yield), который преобразует все буквенные символы в строчные.
from string import ascii_lowercase


def lower(crs):
    for text in crs:
        yield text.lower


text = input("Введите текст")
print(text)
