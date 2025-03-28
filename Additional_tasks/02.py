# Давайте створимо простий калькулятор. Напишіть програму, яка запитує у
# користувача два цілих числа і виконує такі дії:
# - обчислює суму та виводить результат.
# - обчислює різницю і виводить результат (перше число мінус друге число).
# - обчислює добуток та виводить результат.
# - обчислює ділення (результат поділу першого числа на друге) та виводить
#   результат.
# - обчислює залишок від поділу першого числа на друге та виводить результат.
# - Зводить перше число у ступінь другого числа та виводить результат.

# Приклад:
# Введіть перше число: 5
# Введіть друге число: 2

# Сума: 7
# Різниця: 3
# Добуток: 10
# Ділення: 2.5
# Залишок від ділення: 1
# Перше число у ступені другого числа: 25

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
print('Сума:', a + b)
print('Різниця:', a - b)
print('Добуток:', a * b)
print('Ділення:', a / b)
print('Залишок від ділення:', a % b)
print('Перше число у ступені другого числа:', a ** b)

# Рішення викладача:

first_number = int(input("Введіть перше число: "))
second_number = int(input("Введіть друге число: "))

print("Сумма: ", first_number + second_number)
print("Різниця: ", first_number - second_number)
print("Добуток: ", first_number * second_number)
print("Ділення: ", first_number / second_number)
print("Залишок від розподілу: ", first_number % second_number)
print("Перше число у ступені другого числа: ", first_number ** second_number)