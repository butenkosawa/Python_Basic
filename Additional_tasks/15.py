# Напишіть програму, яка запитує у користувача рядок і визначає, чи є вiн
# панграмою. Панграма - це фраза, що містить усі літери алфавіту. Програма
# повинна ігнорувати регістр літер та пробіли під час перевірки панграми.
# Виведіть відповідне повідомлення на екран за допомогою команди print.
# Розв'язати задачу для латиниці.
#
# Приклад:
# Введіть рядок: The quick brown fox jumps over the lazy dog
# Рядок є панграмою.

from string import ascii_lowercase

text = "The quick brown fox jumps over the lazy dog"

text_set = set(text.lower().replace(' ', ''))
lett_set = set(ascii_lowercase)

if text_set == lett_set:
    print("Рядок є панграмою.")

    # Рішення викладача:
alphabet = "ABCDEFGIJHKLMNOPQRSTUVWXYZ"
s = input("Введіть рядок:")
i = 0
while i < len(alphabet):
    if alphabet[i] in s.upper():
        i += 1
    else:
        print("Рядок не є панграмою")
        break
else:
    print("Рядок є панграмою")
