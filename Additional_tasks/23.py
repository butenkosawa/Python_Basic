# Напишіть програму, яка приймає список чисел і повертає суму, мінімальне та
# максимальне значення зі списку. Використовуйте функцію для обробки списку
# чисел та повернення трьох значень. Виведіть результат на eкран за допомогою
# команди print.
#
# Приклад:
# Введіть числа через кому та пробіл: 3, 7, 2, 9, 1, 5
# Сума чисел: 27
# Мінімальне значення: 1
# Максимальне значення: 9

number = input("Введіть числа через кому та пробіл: ")
number_list = [int(el) for el in number if el.isdigit()]
print(f"Сума чисел: {sum(number_list)}")
print(f"Мінімальне значення: {min(number_list)}")
print(f"Максимальне значення: {max(number_list)}")

# Рішення викладача:

def vse(a):
    for i in range(len(a)):
        a[i] = int(a[i])
    return sum(a), max(a), min(a)


x = input("Введіть числа: ").split(', ')
s, mx, mn = vse(x)
print("Сума чисел:", s)
print("Мінімальне значення:", mx)
print("Максимальне значення:", mn)