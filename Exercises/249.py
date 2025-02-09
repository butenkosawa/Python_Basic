# Програма отримує на вхід послідовність цілих невід’ємних чисел, кожне число вводиться в окремому рядку.
# Послідовність завершується числом 0, при зчитуванні якого програма повинна закінчити свою роботу і
# вивести кількість членів послідовності (не рахуючи завершального числа 0).

# num = int(input('Enter positive numbere: '))
# sum = 0
#
# while num > 0:
#     sum += 1
#     num = int(input('Enter positive number: '))

sum = 0

while True:
    num = int(input('Enter positive number: '))
    if num == 0:
        break
    sum += 1

print(sum)