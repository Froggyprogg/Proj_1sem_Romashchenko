# Составить генератор (yield), который преобразует все буквенные символы в строчные.


def izm(crs: str):
    for ch in crs:
        yield ch.lower()


text = input("Введите текст")
print(''.join(izm(text)))
