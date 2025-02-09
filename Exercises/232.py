# Дано n чисел. Визначте, скільки з них дорівнюють нулю, і виведіть цю кількість.
# Спочатку вводиться число n, потім вводиться рівно n цілих чисел.

n = int(input("Enter number, n: "))
numm = input(f"Enter {n} numbers separated by space: ").split()
print(numm)
nuls = 0

for item in numm:
    if int(item) == 0:
        nuls += 1

print(nuls)
