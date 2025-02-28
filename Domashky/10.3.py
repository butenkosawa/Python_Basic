# Ваша функція is_even повинна повертати True якщо число парне, і False якщо
# число непарне.
# Вхідні дані: Ціле число.
# Вихідні дані: Логічний тип.
#
# def is_even(digit):
#     """ Перевірка чи є парним число """
#     pass
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')

def is_even(number: int) -> bool:
    """
    The function checks whether a number is even.

    :param number: integer number
    :return: True if number is even, else False
    """
    return True if number % 2 == 0 else False


print(is_even(2))
print(is_even(5))
print(is_even(0))