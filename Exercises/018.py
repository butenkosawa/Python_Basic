asii_value = int(input('Введіть ASCII значення: '))
sym_value = input('Введіть символ: ')

sym_res = chr(asii_value) # ASCII значенням -> Символ
asii_res = ord(sym_value) # Символ -> ASCII значення

print('ASII:', asii_value, 'Cимвол:', sym_res)
print('Cимвол:', sym_value, 'ASII:', asii_res)
