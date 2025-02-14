# Написати програму для обчислення суми цифр цілого числа n.
# Програма має враховувати, що на вхід може подаватися ціле від’ємне число.

n = int(input('Enter integer number: '))
print('Summa of digits:', sum([int(dg) for dg in list(str(abs(n)))]))