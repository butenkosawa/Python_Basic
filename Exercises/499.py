# Напишіть програму, яка отримує на вхід чотирьохзначне додатне десяткове число
# та генерує з цифр цього числа мінімально можливе чотирьохзначне число та
# максимально можливе чотирьохзначне число. У першому рядку задано одне чотирьохзначне число.
# Виведіть у другому рядку два числа - найменше чотирьохзначне число та найбільше чотирьохзначне число,
# які можна отримати з цифр даного числа. Числа розділяйте одним пропуском.
# Вхідні дані:
# 1390
# 1010
# 5173
# Вихідні дані:
# 1039 9310
# 1001 1100
# 1357 7531

number = 1010
digits = sorted(list(str(number)))

if digits[0] == '0':
    digits[:2] = digits[1::-1]

number_min = int("".join(digits))
number_max = int("".join(sorted(digits, reverse=True)))

print(number)
print(number_min, number_max)


