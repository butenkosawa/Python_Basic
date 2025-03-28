# Напишіть програму, яка запитує у користувача рядок і визначає, чи містить
# він тільки унікальні символи. Якщо всі символи в рядку унікальні, виведіть
# відповідне повідомлення на екран. В іншому випадку виведіть повідомлення
# про те, які символи повторюються. Не використовуйте множини для
# перевірки унікальності символів.
#
# Приклад:
# Введіть рядок: Python
# Усі символи у рядку унікальні.
# Введіть рядок: Hello Konal
# Символи 'l' і 'o' повторюються.

text = "Python is one of the top programming languages in the world."
letters = []

for lt in text.replace(" ", ""):
    if text.count(lt) >= 2:
        if lt not in letters:
            letters.append(lt)

if len(letters) == 0:
    print("Усі символи у рядку унікальні.")
elif len(letters) == 1:
    print(f"Символ {letters[0]} повторюються")
else:
    print(f"Символи {', '.join(letters[:-1])} та '{letters[-1]}' повторюються.")

# Рішення викладача:
string = input("Введіть рядок: ").lower()
i = 0
symbols = []
while i < len(string):
    if string[i+1:].find(string[i]) != -1 and f"'{string[i]}'" not in symbols:
        symbols.append(f"'{string[i]}'")
    i += 1

if symbols:
    if len(symbols) == 1:
        res = symbols[0]
    else:
        res = ", ".join(symbols[:-1])
        res += f" і {symbols[-1]}"
    print(f"Символи {res} повторюються.")
else:
    print("Усі символи у рядку унікальні.")