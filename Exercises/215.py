# Напишіть програму, яка друкує в одному рядку через пропуск усі парні числа від 1 до n
# (1 < n ≤ 100, n - ціле число, яке вводить користувач). Використайте оператор continue.

n = int(input("Enter number, 1 < n ≤ 100: "))
mult_number = 2

for num in range (1, n + 1):
    if num % mult_number != 0:
        continue
    print (num, end=' ')
