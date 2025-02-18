# Вводиться список цілих чисел в одному рядку через пропуск.
# Надрукуйте всі елементи, які перевищують попередній елемент списку,
# через пропуск в новому рядку в порядку їх розміщення у списку.

num = [int(dg) for dg in input('Enter numbers, separated by space: ').split()]

for i in range(1, len(num)):
    if num[i] > num[i - 1]:
        print(num[i], end=' ')