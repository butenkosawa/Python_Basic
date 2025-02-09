# Визначити суму всіх трицифрових чисел, які діляться націло на n, де n - ціле число, яке вводить користувач.

n = int(input("Enter number n: "))
summ = 0

for i in range(100, 1000):
    if i % n == 0:
        summ += i
        # print(i, summ, sep='\t' * 2)

print(summ)
