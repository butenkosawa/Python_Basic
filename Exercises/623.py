# Напишіть функцію, яка повертає зі списку найменше і найбільше числа.
# Вхідні дані:
# 6 1 9 -5 23 15 44 31 10 -14 7 8
# Вихідні дані:
# (-14, 44)

def minmax_in_list(lst: list):
    return min(lst), max(lst)


print(minmax_in_list([6, 1, 9, -5, 23, 15, 44, 31, 10, -14, 7, 8]))