# Напишіть програму, яка друкує усі непарні числа з інтервалу [1, b],
# де b - ціле число, яке вводить користувач. Не можна використовувати конструкцію розгалуження.

# b = int(input("Enter number, n: "))
b = 8

for i in range(1, b+1, 2):
    print(i, end=' ')