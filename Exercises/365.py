# Користувач вводить рядок, у якому містяться слова, знаки пунктуації,
# причому усі слова записуються разом і перша літера кожного слова є великою.
# Напишіть програму, яка виводить рядок, у якому введені слова розділені пропусками.

txt = input('Enter any text: ')
txt_sep = []

for sym in txt:
    if sym.isupper():
        txt_sep.append(' ' + sym)
    else:
        txt_sep.append(sym)

print(''.join(txt_sep).strip(' '))