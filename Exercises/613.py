# Напишіть функцію для визначення найбільшого з трьох цілих чисел з використанянм вбудованої функції max().
# Вхідні дані:
# 1 2 2
# 12 8 35
# 1 1 1
# Вихідні дані:
# 2
# 35
# 1


def max_of_numbers(*args):
    return max(args)


print(max_of_numbers(1, 2, 2))
print(max_of_numbers(12, 8 ,35))
print(max_of_numbers(1, 1, 1))