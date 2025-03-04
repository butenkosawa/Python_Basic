# Напишіть функцію, яка приймає послідовність цілих чисел та ціле число n,
# що вводяться на окремих рядках. Функція повертає True, якщо вказане число
# знаходиться всередині списку, або False у протилежному випадку.
# Вхідні дані:
# 3 6 9 10 23 14
# 23
# Вихідні дані:
# True

def contains_number(sequence, n):
    return n in sequence


input_sequence = [3, 6, 9, 10, 23, 14]
n = 23

result = contains_number(input_sequence, n)

print(result)