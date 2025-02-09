# Напишіть програму, яка виводить усі трицифрові числа,
# сума цифр яких дорівнює деякому значенню n, яке вводить користувач.

n = int(input("Enter n: "))
total = 0

for i in range(100, 1000):
    num12, num3 = divmod(i, 10)
    num1, num2 = divmod(num12, 10)
    if num1 + num2 + num3 == n:
        print(i)
