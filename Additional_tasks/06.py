# Напишіть програму, яка запитує у користувача два логічні значення (True або
# False) і виводить результати наступних логічних операцій:

# Логічне І (and) між двома значеннями.
# Логічне АБО (or) між двома значеннями.
# Логічне НЕ (not) кожного значення.
# Результат порівняння двох значень на рівність.
# Результат порівняння двох значень на нерівність.

# Результати мають бути виведені за допомогою print. Введену строку "True"
# або "False" треба привести до булевого типу "True" або "False" і потім вже
# над булевими значеннями проводити операції.

logic_1 = input('Введіть одне з логічних значень (True або False): ')
logic_2 = input('Введіть одне з логічних значень (True або False): ')

logic_1 = False if logic_1 == 'False' else bool(logic_1)
logic_2 = False if logic_2 == 'False' else bool(logic_2)

print('Логічне І (and): ', logic_1 and logic_2)
print('Логічне АБО (or): ', logic_1 or logic_2)
print('Логічне НЕ (not): ', logic_1 is not logic_2)
print('Порівняння двох значень на рівність: ', logic_1 == logic_2)
print('Порівняння двох значень на нерівність): ', logic_1 != logic_2)

# Рішення викладача:

a = input("Введите значение a (True или False):")
b = input("Введите значение b (True или False):")
a = True if a.lower() == "true" else False
b = True if b.lower() == "true" else False

print("a and b =", a and b)
print("a or b =", a or b)
print("not a =", not a)
print("not b =", not b)
print("a == b =", a == b)
print("a != b =", a != b)

