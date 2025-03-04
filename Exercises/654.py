# Напишіть функцію для визначення, чи рік високосний чи ні.
# Вхідні дані:
# 2023
# 2020
# Вихідні дані:
# False
# True

def leap_year(year):
    return any([(year % 4 == 0 and year % 100 != 0), (year % 400 == 0)])


print(leap_year(2023))
print(leap_year(2020))