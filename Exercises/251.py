# Визначте середнє значення всіх елементів послідовності, яка завершується числом 0.
# Вводиться послідовність цілих чисел, що закінчується числом 0
# (саме число 0 в послідовність не входить, а використовується як ознака її закінчення).

sum = 0
count_pass = 0
average = 0

while True:
    num = int(input('Enter number: '))
    if num == 0:
        break
    sum += num
    count_pass += 1
    average = sum / count_pass

print(f"{average:.{1}f}")
print(average)