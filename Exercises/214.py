# Напишіть програму, яка підраховує додатні і від’ємні числа, а також нулі,
# введені користувачем, і виводить їхню кількість в один рядок з одним пропуском між ними.

numbers = input("Enter numbers separated by a space: ").split()

pos_num = 0
neg_num = 0
nul_num = 0

print(numbers)

for num in numbers:
    if int(num) > 0:
        pos_num += 1
    elif int(num) < 0:
        neg_num += 1
    else:
        nul_num += 1

print(f"{pos_num} {neg_num} {nul_num}")