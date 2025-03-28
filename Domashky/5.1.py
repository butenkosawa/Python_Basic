# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
#
# Змінна не може:
#
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
#
# Список зареєстрованих слів можна взяти із keyword.kwlist.
#
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
#
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))

# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

from string import punctuation
from keyword import kwlist

name_of_var = input('Enter name of variable: ')

if name_of_var.startswith('_') and len(name_of_var) == 1:
    print('True')
else:
    if name_of_var[0].isdigit():
        print('False')
    elif name_of_var in kwlist:
        print('False')
    elif not name_of_var.islower():
        print('False')
    elif len(name_of_var) > 0:
        for sym in punctuation.replace('_',' '):
            if sym in name_of_var:
                print('False')
                break
        else:
            print('True')

# Рішення викладача

result = True
name = input("Введіть рядок: ")
if len(name) > 1 and all(char == '_' for char in name):
    result = False
if name[0].isdigit():
    result = False
if any(char.isupper() or char in string.whitespace or
       char in string.punctuation.replace('_', '') for char in name):
    result = False
if name in keyword.kwlist:
    result = False

print(result)