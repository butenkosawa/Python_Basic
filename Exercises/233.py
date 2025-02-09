# Дано n цілих чисел. Кожне число вводиться в окремому рядку. Обчисліть суму чисел.

n = 10
summ = 0

for i in range(0, n):
    num = int(input("Enter number: "))
    # print(num)
    summ += num

print(summ)
