# Напишіть програму, яка запитує у користувача натуральне десяткове число і
# виводить його двійкове уявлення. Реалізуйте алгоритм переведення числа в
# двійкову систему числення, використовуючи основні концепції подання чисел
# (підказка: через розподіл із залишком). Виведіть отримане подання числа на екран.
#
# Приклад:
# Введіть натуральне десяткове число: 123
# Двійкове уявлення числа: 1111011

n = int(input('Введіть натуральне десяткове число: '))
print('Десяткове число:', n, sep='\t')
dg10 = []
print(bin(n))

while n > 0:
    dg10.insert(0, n % 2)
    n = n // 2

print('Двійкове число:', "".join([str(dg) for dg in dg10]), sep='\t' * 2)

# Рішення викладача:

number = int(input('Введіть натуральне десяткове число:'))
res = ''
while number > 0:
    res = str(number % 2) + res
    number //= 2
print('Двійкове уявлення числа:', res)