# Напишіть програму, яка запитує користувача три числа і виводить їх у порядку
# зростання, розділені комою. Використовуйте умовні оператори та вкладені
# умови для вирішення завдання. Передбачається, що це три числа різні.

# Приклад:
# Введіть перше число: 5
# Введіть друге число: 2
# Введіть третє число: 7

# Числа в порядку зростання: 2, 5, 7
a = int(input('Enter number, a = '))
b = int(input('Enter number, b = '))
c = int(input('Enter number, c = '))
large, middle, small = 0, 0, 0

if a > b and a > c:
    if b > c:
        large, middle, small = a, b, c
    else:
        large, middle, small = a, c, b
elif b > a and b > c:
    if a > c:
        large, middle, small = b, a, c
    else:
        large, middle, small = b, c, a
elif c > a and c > b:
    if a > b:
        large, middle, small = c, a, b
    else:
        large, middle, small = c, b, a

print('{}, {}, {}'.format(small, middle, large))

# Рішення викладача:

first_number = int(input('Введіть перше число: '))
second_number = int(input('Введіть друге число: '))
third_number = int(input('Введіть третє число: '))

if first_number > second_number:
    first_number, second_number = second_number, first_number
if second_number > third_number:
    second_number, third_number = third_number, second_number
if first_number > second_number:
    first_number, second_number = second_number, first_number

print(f'Числа в порядку зростання: {first_number}, {second_number}, {third_number}')