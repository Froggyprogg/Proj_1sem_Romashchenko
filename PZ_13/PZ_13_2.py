# Составить генератор (yield), который преобразует все буквенные символы в строчные.


def izm(text_start):
    for n in text_start:
        yield text_start.lower()
        print(text_start)


text_start = iter(input("Введите текст"))
text_end = izm(text_start)
print(text_end)
