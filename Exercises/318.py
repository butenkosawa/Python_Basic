# Дано натуральне число. Знайти число, що отримується видаленням з вхідного усіх зазначених цифр.

num = int(input('Enter integer number: '))
dig = input('Enter digit for deleting: ')

print(int(''.join([i for i in str(num).split(dig) if i != ''])))
print(int(str(num).replace(dig, '')))
