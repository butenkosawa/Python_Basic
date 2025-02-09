# Дано ціле число n, яке вводить користувач. Необхідно обчислити значення виразу 1! +2! +3! + …​ + n!.

n = 5
fact = 1
summ = 0

for i in range(1, n+1):
    fact *= i
    summ += fact

print(summ)