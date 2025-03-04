# Напишіть функцію, яка перевіряє, чи подана послідовність порожня чи ні.
# Вхідні дані:
# Різні типи послідовностей (список, кортеж, словник)
# Вихідні дані:
# True чи False

def is_empty_sequence(sequence):
    return len(sequence) == 0

print(is_empty_sequence([]))
print(is_empty_sequence((2,)))