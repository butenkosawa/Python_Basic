# Напишіть програму, яка запитує у користувача рядок і перетворює його,
# видаляючи всі голосні літери з рядка. Використовуйте метод replace() для
# заміни голосних літер на порожній рядок. Виведіть перетворений рядок на
# екран за допомогою команди print.
#
# Приклад:
# Введіть рядок: Hello, world!
# Результат: Hll, wrld!

text = "Python is one of the top programming languages in the world."
vowel = 'aeiouAEIOU'
print(text)

for lt in vowel:
    if lt in text:
        text = text.replace(lt, '')

print(text)

# Рішення викладача:

aei = "AEIOUY"
s = input("Введіть рядок: ")
i = 0
while i < len(aei):
    s = s.replace(aei[i], "")
    s = s.replace(aei[i].lower(), "")
    i += 1
print("Результат: ", s)