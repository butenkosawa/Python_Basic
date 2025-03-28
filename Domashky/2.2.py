# Необхідно "перевернути" 5-ти значне число

number = int(input('Введіть довільне п’ятизначне число: '))

# num1 = number//10000
# num2 = number%10000//1000
# num3 = number%10000%1000//100
# num4 = number%10000%1000%100//10
# num5 = number%10000%1000%100%10

num1, a = divmod(number, 10000)
num2, b = divmod(a, 1000)
num3, c = divmod(b, 100)
num4, num5 = divmod(c, 10)

print(num5 * 10000 + num4 * 1000 + num3 * 100 + num2 * 10 + num1)
# print(num5, num4, num3, num2, num1, sep='')

# Рішення викладача
# запитуємо у користувача 5-ти значне число
number = int(input("Enter a 5-digit number: "))

# перша цифра
tens_of_thousands = number // 10000

# друга цифра
thousands = (number // 1000) % 10

# третя цифра
hundreds = (number // 100) % 10

# четверта цифра
tens = (number // 10) % 10

# п'ята цифра
units = number % 10

# формуємо нове число,що складається з цифр у зворотному порядку
flipped_number = (units * 10000) + (tens * 1000) + (hundreds * 100) + (thousands * 10) + tens_of_thousands

# виводимо перевернуте число
print(flipped_number)