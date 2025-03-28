# Напишіть функцію-генератор prime_generator, яка повертатиме прості числа.
# Верхня межа цього діапазону визначається параметром цієї функції.
# Наприклад, виклик функції list(prime_generator(10)) повинен відповідати
# послідовності з чисел [2, 3, 5, 7].
# Наступне число в цій послідовності - 11 і воно більше ніж 10 тому воно не потрапляє в цей ряд

# def prime_generator(end):
#     pass
#
from inspect import isgenerator


def prime_generator(end):
    number = 2
    while number <= end:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number
        number += 1

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')


# Рішення викладача:

def prime_generator(end):
    for i in range(2, end + 1):
        if all(i % n != 0 for n in range(2, i)):
            yield i
