# Напишіть функцію, яка отримує значення середньомісячної кількості
# опадів по місяцях (в мм) і повертає загальний обсяг опадів протягом року,
# середньорічну кількість опадів, назви місяців та значення з найвищим
# та найменшим числом опадів протягом року.
# Вхідні дані:
# 22 22 24 49 72 98 101 82 51 40 36 24
# Вихідні дані:
# (621.0, 51.75, (101.0, 'July'), (22.0, 'January'))

def precipitations(*args):
    months = ('January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December')
    precip_year = dict(zip(args, months))
    max_precip = (float('{:.1f}'.format(max(args))), precip_year.get(max(args)))
    min_precip = (float('{:.1f}'.format(min(args))), precip_year.get(min(args)))
    return float('{:.1f}'.format(sum(args))), round(sum(args) / len(args), 2), max_precip, min_precip


print(precipitations(22, 22, 24, 49, 72, 98, 101, 82, 51, 40, 36, 24))


