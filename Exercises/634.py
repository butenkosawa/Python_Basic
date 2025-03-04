# Python має вбудовану функцію __doc__ для друку документації для всіх вбудованих функцій.
# Наприклад, для доступу до документації функції abs(), слід використати такий запис:
# print(input.__doc__). Напишіть функцію для обчислення квадрата цілого числа.
# В тілі функції додайте багаторядковий коментар про те, що робить функція.
# Викличте функцію і перегляньте її документацію.
# Вхідні дані:
# 9
# Вихідні дані:
# 81
# Return the square value of the input number.
#     The input number must be integer.

def square_number(num):
    """Return the square value of the input number

    :param num: The input number must be integer
    :return:
    """
    return num ** 2


print(square_number(9))
print(square_number.__doc__)
