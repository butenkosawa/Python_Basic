# Напишіть програму для друку чисел від 0 до n включно і
# виведення в один рядок через один пропуск (n - ціле число, яке вводить користувач).

n = int(input("Enter number n: "))

for i in range (0, n + 1):
    print(i, end=' ')