# Дано рядок. Визначити порядковий номер першої вказаної букви. Якщо такої літери немає, вивести нуль.

# txt = 'Armed Forces'
txt = input('Enter any text: ')
char = input('Enter character: ')
print(txt.index(char) + 1)
