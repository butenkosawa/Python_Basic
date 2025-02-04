# Напишіть програму для перетворення введених секунд у кількість днів, годин, хвилин та секунд.

seconds = int(input('Введіть кількість секунд: '))
days, a = divmod(seconds, 86400)
hours, b = divmod(a, 3600)
minutes, secs = divmod(b, 60)
print(days, 'днів', hours, 'годин', minutes, 'хвилин', secs, 'секунд')
