# Напишіть функцію для перетворення літер введеного рядка у великі,
# якщо він містить принаймні n великих літер в перших m символах.
# Спочатку вводиться сам рядок, а в з нового рядка - числа n і m.
# Вхідні дані:
# Python
# 1 3
# Ruby
# 2 2
# Вихідні дані:
# PYTHON
# Ruby

def transform_letters():
    string = input('Enter string: ')
    condition = input('Enter the number of "N" uppercase letters in the first "M" characters: ')

    for char in condition:
        if not char.isdigit():
            condition = condition.replace(char, '')

    n, m = tuple(map(lambda x: int(x), condition))

    for char in string[:m]:
        if char.isupper():
            n -= 1

    return string.upper() if n == 0 else string

print(transform_letters())


