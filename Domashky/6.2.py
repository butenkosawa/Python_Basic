# Ваше завдання — написати програму, яка переводить число у формат часу у
# читальному вигляді. Користувач повинен ввести число більше або дорівнює 0 і
# менше ніж 8640000. Число, яке є кількістю секунд, необхідно перевести в дні,
# години, хвилини та секунди. Ну і додатковим завданням є турбота про виведення.
#
# Слово "день" підбирається на основі кількості днів, а години, хвилини і
# секунди повинні заповнюватися нулями при одноцифрових значеннях.
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі
# 24 * 60 * 60 сек. Тобто використовуючи функцію divmod або методи поділу
# // і % вам необхідно знайти відповідну кількість днів, годин, хвилин, а те
# що залишиться - це секунди, які менше 60 ;)
# Доповнити провідними нулями можна за допомогою методу zfill(2)
#
# Приклад:
# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

seconds = int(input('Введіть кількість секунд від 0 до 8640000: '))

while seconds < 0 or seconds > 8640000:
    seconds = int(input('''Введена кількість секунд знаходиться поза межами діапазону.
Введіть коректну кількість: '''))

dd, seconds = divmod(seconds, 24*60*60)
hh, seconds = divmod(seconds, 60*60)
mm, ss = divmod(seconds, 60)
days = ''

if dd in range(11, 15):
    days = 'днів'
elif dd % 10 == 0 or dd % 10 in range(5, 10):
    days = 'днів'
elif dd % 10 == 1:
    days = 'день'
else:
    days = 'дні'

print(f'{dd} {days}, {str(hh).zfill(2)}:{str(mm).zfill(2)}:{str(ss).zfill(2)}')

# Рішення викладача

user_num = int(input('Input number less or equal then 8640000: '))

seconds_tpl = divmod(user_num, 60)
minutes_tpl = divmod(seconds_tpl[0], 60)
hours_tpl = divmod(minutes_tpl[0], 24)

seconds = str(seconds_tpl[1]).zfill(2)
minutes = str(minutes_tpl[1]).zfill(2)
hours = str(hours_tpl[1]).zfill(2)
days = str(hours_tpl[0])

if days[-1] not in ('1', '2', '3', '4') or (len(days) > 1 and days[-2] == '1'):
    word_days = 'днів'
elif days[-1] == '1':
    word_days = 'день'
else:
    word_days = 'дні'

print(days, word_days + ",", hours + ":" + minutes + ":" + seconds)