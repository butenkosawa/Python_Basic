# Виведення числа в стовпчик

number = int(input('Введіть довільне чотиризначне число: '))

# num1 = number//1000
# num2 = number%1000//100
# num3 = number%1000%100//10
# num4 = number%1000%100%10

num1, a = divmod(number, 1000)
num2, b = divmod(a, 100)
num3, num4 = divmod(b, 10)

print(num1)
print(num2)
print(num3)
print(num4)


# Рішення викладача

# запитуємо у користувача 4-х значне число
number = int(input("Enter a 4-digit number: "))

# перша цифра
digit1 = number // 1000

# друга цифра
digit2 = (number // 100) % 10

# третя цифра
digit3 = (number // 10) % 10

# Четверта цифра
digit4 = number % 10

# виводимо цифри у стовпець
print(digit1)
print(digit2)
print(digit3)
print(digit4)