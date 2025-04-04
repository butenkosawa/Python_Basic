# Реалізуйте генераторну функцію (з використанням оператора yield), яка повертатиме
# по одному члену числової послідовності, закон якої задається за
# допомогою функції користувача. Крім цього параметром генераторної функції
# повинні бути значення першого члена прогресії та кількість членів, що
# видаються послідовності (n). Генератор повинен зупинити свою роботу з
# досягнення n-го члена.
#
# Підказка: це завдання дуже схоже на нескінченний лічильник з матеріалів
# лекції! Потрібно лише обмежити кількість видаваних генератором значень!
#
# def pow(x):
#     return x ** 2
#
# def some_gen(begin, end, func):
#     """
#      begin: перший елемент послідовності
#      end: кількість елементів у послідовності
#      func: функція, яка формує значення для послідовності
#     """
#     ....
#     yield begin


from inspect import isgenerator

def increase_number_by_half(number):
    return number + number / 2


def some_gen(begin, end, func):
    while end > 0:
        yield round(begin, 2)
        begin = func(begin)
        end -= 1


gen = some_gen(4, 7, increase_number_by_half)
print(isgenerator(gen))
print(list(gen))


# Рішення викладача

from inspect import isgenerator


def pow(x):
    return x ** 2


def some_gen(begin, end, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    current = begin
    for _ in range(end):
        yield current
        current = func(current)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')