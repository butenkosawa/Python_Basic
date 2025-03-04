# Напишіть функцію, яка приймає ціле число і друкує інформацію про парність чи непарність числа.
# Вхідні дані:
# 2
# 9
# Вихідні дані:
# True
# False

def if_even(number):
    return number % 2 == 0


print(if_even(2))
print(if_even(9))