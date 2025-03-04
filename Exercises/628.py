# Напишіть функцію для друку парних чисел із заданої послідовності цілих чисел.
# Вхідні дані:
# 32 4 7 9 11 13 15 8
# Вихідні дані:
# 32 4 8

def print_even(numbers: list):
    for number in numbers:
        if number % 2 ==0:
            print(number, end=' ')

print_even([32, 4, 7, 9, 11, 13, 15, 8])