# # Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# # яка повертатиме всі символи між ними включно.
# # Жодних перевірок на помилку робити не треба, мінімальне значення завжди
# # менше або дорівнює максимальному.
# # Підказка: Використовуйте модуль string , у якому є string.ascii_letters, з
# # усім набором потрібних букв
# #
# # Приклад:
# # "a-c" -> abc
# # "a-a" -> a
# # "s-H" -> stuvwxyzABCDEFGH
# # "a-A" -> abcdefghijklmnopqrstuvwxyzA

from string import ascii_letters
letters = input('Enter 2 letters separated by "-": ')
index_lt1 = ascii_letters.index(letters[0])
index_lt2 = ascii_letters.index(letters[-1])

if letters[0].islower() and letters[-1].isupper():
    print(ascii_letters[index_lt1 : index_lt2 + 1])
elif letters[0].isupper() and letters[-1].islower():
    print(ascii_letters[index_lt1 :: -1]) if index_lt2 == 0 else print(ascii_letters[index_lt1 : index_lt2 - 1 : -1])
elif letters[0] <= letters[-1]:
    print(ascii_letters[index_lt1 : index_lt2 + 1])
else:
    print(ascii_letters[index_lt1 :: -1]) if index_lt2 == 0 else print(ascii_letters[index_lt1 : index_lt2 - 1 : -1])

# Рішення викладача

import string

ascii_str = string.ascii_letters
user_letters = input("Enter a range of letters in the format 'a-z': ")

first_letter_index = ascii_str.index(user_letters[0])
second_letter_index = ascii_str.index(user_letters[-1])
print(ascii_str[first_letter_index:(second_letter_index + 1)])
