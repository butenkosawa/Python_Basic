# Напишіть програму, яка запитує у користувача число N і виводить на
# Екран таблицю множення від 1 до N. Використовуйте вкладений цикл for для
# створення таблиці множення. Виведіть результат на екран за допомогою print.
#
# Приклад:
# Введіть число N: 5
# Таблиця множення:
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

n = 10

for i in range(1, n+1):
    for j in range(1, n+1):
        print(i * j, end="\t")
    print()