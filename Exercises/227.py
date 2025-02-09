# При заданому користувачем значенні цілого числа n ≥ 2 обчислити вираз 1 × 2 + 2 × 3 + … + (n - 1) × n

n = int(input("Enter number n: "))
summ = 0

for i in range(1, n):
    summ += i * (i + 1)

print(summ)