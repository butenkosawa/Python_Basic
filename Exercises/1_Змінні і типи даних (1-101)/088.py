# Розрахунок суми чисел 4 значного цілого числа
number = int(input('Enter a 4-digit number: '))

num1, a = divmod(number, 1000)
num2, b = divmod(a, 100)
num3, num4 = divmod(b, 10)

result = num1 + num2 + num3 + num4

print(result)
