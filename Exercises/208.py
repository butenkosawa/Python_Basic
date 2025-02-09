# Напишіть програму для виведення усіх цілих чисел від 20 до n включно (n > 20),
# де n - ціле число, яке вводить користувач.

n = int(input("Enter number, n > 20: "))
start_num = 20

for i in range (start_num, n + 1):
    print (start_num)
    start_num += 1