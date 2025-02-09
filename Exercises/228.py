# Напишіть програму для обчислення виразу 1/2 + 2/3 + 3/4 + … + n/(n + 1) із заданим n, яке вводить користувач (n > 0).

n = int(input("Enter number n: "))
summ = 0

for i in range(1, n+1):
    summ += i / (i + 1)

print(f"{summ:.{2}f}")