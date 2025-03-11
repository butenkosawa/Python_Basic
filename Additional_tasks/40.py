# Напишіть функцію, яка приймає на вхід список чисел та повертає суму
# квадратів тільки парних чисел зі списку, використовуючи функціональні
# підходи (наприклад, map, filter та reduce).
#
# Приклад:
# Введіть числа: 4, 6, 3, 4, 2, 3, 9, 0, 7
# Результат: 72
from functools import reduce


def summ_of_even(*args):
    return sum(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, args)))

print(summ_of_even(4, 6, 3, 4, 2, 3, 9, 0, 7))