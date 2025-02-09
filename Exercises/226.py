# Знайти суму 1**2 + 2**2 + 3**2 + … + n**2 при заданому користувачем значенні цілого числа n.

n = int(input("Enter number n: "))
summ = 0

for i in range(1, n+1):
    summ += i ** 2

print(summ)