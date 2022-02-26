# Составить генератор (yield), который преобразует все буквенные символы в строчные.
from string import ascii_lowercase


text = input("Введите текст")

def swapcase(text):
    yield from [text.swapcase]

print(text)
