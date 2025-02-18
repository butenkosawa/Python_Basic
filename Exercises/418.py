# Напишіть програму для доступу до індексу цілочисельних елементів списку.
# Числа списку вводяться на одному рядку через пропуск.

num = [int(dg) for dg in input('Enter numbers, separated by space: ').split()]

for i, dg in enumerate(num):
    print(i, dg)
