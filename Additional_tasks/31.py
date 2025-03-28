# Напишіть програму, яка використовує рекурсію для обчислення суми цифр
# Числа. Створіть функцію sum_digits, яка приймає один аргумент – число,
# для якого потрібно обчислити суму цифр. Використовуйте умову виходу з
# рекурсії, коли число складається з однієї цифри. Виведіть результат на екран.
#
# Приклад:
# Введіть число: 12345
# Сума цифр числа 12345 дорівнює 15

def sum_digits(number):
    if number < 10:
        return number
    return number % 10 + sum_digits(number // 10)

print(sum_digits(12345))

# Рішення викладача:

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n//10)


number = int(input("Введіть число: "))
print(f"Сума цифр числа {number} дорівнює {sum_digits(number)}", )