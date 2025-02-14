# Дано послідовність символів довжини n (n ≥ 1). Перевірити баланс круглих дужок в цьому виразі
# (кожна відкита дужка має свою закриту дужку). Наприклад, при введенні виразу (()) ()
# програма повинна повідомити про правильність розстановки дужок (True),
# а при введенні виразу ((()) - про неправильність (False).
# Напишіть програму, яка може перевіряти баланс дужок в арифметичних виразах, тексті і т. д.
# Вхідні дані:
# (3y + 21)(12 - (x + 5))
# (61x + 15(y + 2)
# Вихідні дані:
# True
# False

txt = "(3y + 21((12 - (x + 5))"
count_brackets = 0
el = 0

while el < len(txt):
    if txt[el] == '(':
        count_brackets += 1
        if txt[el + 1] == ')':
            print('False')
            break
    elif txt[el] == ')':
        count_brackets -= 1
        if count_brackets < 0:
            print('False')
            break
    el += 1

print('True') if count_brackets == 0 else print('False')


# brackets = "".join([sym for sym in txt if sym == "(" or sym == ")"])
# print(brackets)
# count_brackets = 0
#
# if brackets[0] == ')':
#     print('False')
# else:
#     for el in brackets:
#         if el == "(":
#             count_brackets += 1
#         elif el == ")":
#             count_brackets -= 1
#     print('True') if count_brackets == 0 else print('False')
