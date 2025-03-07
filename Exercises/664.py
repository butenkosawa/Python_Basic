# Напишіть функцію для сортування рядка в алфавітному порядку без врахування регістру літер.
# Вхідні дані:
# JavaScript
# Python
# Вихідні дані:
# aaciJprStv
# hnoPty

def sort_letters(text: str):
    return "".join(sorted(text, key = lambda x: x.upper()))


print(sort_letters('JavaScript'))
print(sort_letters('Python'))