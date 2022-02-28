# Составить генератор (yield), который преобразует все буквенные символы в строчные.


def lower(text_start):
    yield text_start.lower


text_start = input("Введите текст")
text_end = lower()
print(text_end)
