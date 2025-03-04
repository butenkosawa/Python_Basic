# Напишіть функцію, яка повертає назву пори року для введеного значення номера місяця.
# Вхідні дані:
# 6
# 2
# 9
# 3
# 15
# Вихідні дані:
# summer
# winter
# autumn
# spring
# unknown


def find_season(month: int):
    season = {'winter': (1, 2, 12), 'spring': (3, 4, 5),
              'summer': (6, 7, 8), 'fall/autumn': (9, 10, 11)}

    for key, value in season.items():
        if month in value:
            return key

    return 'unknown'

print(find_season(6))
print(find_season(2))
print(find_season(9))
print(find_season(3))
print(find_season(15))
