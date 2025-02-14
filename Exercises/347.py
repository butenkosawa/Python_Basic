# Напишіть програму для розрахунку довжини рядка без використання функції len().

# txt = input('Enter any text: ')
txt = 'pythonguide.pp.ua'

print(txt.rindex(txt[-1]) + 1)