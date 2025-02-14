# Скласти програму, яка визначає, який з двох введених рядків довший і друкує його.
# Якщо рядки рівні, вивести повідомлення equally

txt1 = input('Enter any text: ')
txt2 = input('Enter any text: ')

if len(txt1) > len(txt2):
    print(txt1)
elif len(txt1) < len(txt2):
    print(txt2)
else:
    print("equally")