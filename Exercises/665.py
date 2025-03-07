# Напишіть функцію для сортування рядка в порядку,
# протилежному алфавітному, без врахування регістру літер.
# Вхідні дані:
# Ruby
# Вихідні дані:
# yuRb

def sort_letters_rev(text: str):
    return "".join(sorted(text, key= lambda x: x.upper(), reverse=True))


print(sort_letters_rev('Ruby'))