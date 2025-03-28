# Напишіть програму, яка запитує у користувача рядок і виводить на екран
# кількість голосних і приголосних літер в ній. Використовуйте функцію len()
# для підрахунку кількості літер. Виведіть результат на екран за допомогою
# команди print. Розв'язати задачу для латиниці.
#
# Приклад:
# Введіть рядок: Hello World
# Кількість голосних літер: 3
# Кількість приголосних літер: 7

text = "Python is one of the top programming languages in the world."
vow = 'aeiou'
con = 'bcdfghjklmnpqrstvwxyz'

vowel = 0
consonant = 0

for lt in text.lower():
    if lt in vow:
        vowel += 1
    elif lt in con:
        consonant += 1

print(f"Кількість голосних літер: {vowel}")
print(f"Кількість приголосних літер: {consonant}")

# Рішення викладача:

aei = "AEIOUY"
bcd = "BCDFGJHKLMNPQRSTVWXZ"
s = input("Введіть рядок:").upper()
i = 0
s1 = ""
s2 = ""
while i < len(s):
    if aei.find(s[i]) >= 0:
        s1 += s[i]
    if bcd.find(s[i]) >= 0:
        s2 += s[i]
    i += 1
print("Кількість голосних літер:", len(s1))
print("Кількість приголосних літер:", len(s2))