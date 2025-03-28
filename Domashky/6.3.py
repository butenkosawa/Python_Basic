# Ваше завдання — написати програму, яка перемножує всі цифри, введені
# користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
# Користувач вводить число з клавіатури.
#
# Приклади:
# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729, Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

number = int(input('Enter number: '))

while number > 9:
    dg_list = [int(dg) for dg in str(number)]
    number = 1
    for dg in dg_list:
        number *= dg

print(number)

# Рішення викладача

user_number = int(input('Enter your integer number: '))

while user_number > 9:
    result = 1
    for i in str(user_number):
        result *= int(i)
    user_number = result

print(user_number)