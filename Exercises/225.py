# Напишіть програму для створення таблиці множення (від 1 до 10) для введеного цілого числа n.

n = int(input("Enter number n: "))

for i in range(1, 11):
    print(f"{n} x {i} =", n * i)