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
