# Написати функцію для перевірки правильності введеної дати.
# Функція приймає 3 аргументи - день, місяць та рік і повертає True,
# якщо така дата є в календарі, і False в протилежному випадку.
# Вхідні дані:
# 04
# 03
# 2029
# 33
# 11
# 2019
# Вихідні дані:
# True
# False

def if_date(day, month, year):
    if any([(int(year) % 4 == 0 and int(year) % 100 != 0), (int(year) % 400 == 0)]):
        if month == '02':
            if int(day) <= 29:
                return True

    elif month == '02':
        if int(day) <= 28:
            return True

    elif month in ('01', '03', '05', '07', '08', '10', '12'):
        if int(day) <= 31:
            return True

    elif month in ('04', '06', '09', '11'):
        if int(day) <= 31:
            return True

    return False


print(if_date('29', '02', '2020'))
print(if_date('04', '03', '2029'))
print(if_date('33', '11', '2019'))