# Напишіть програму, яка отримує три рядки: прізвище, ім’я і по батькові особи,
# а потім виводить на екран ініціали та прізвище.

l_name = input('Enter your Last name: ')
f_name = input('Enter your First name: ')
s_name = input('Enter your Second name: ')

print(f'{f_name.upper()[0]}.{s_name.upper()[0]}.{l_name.title()}')