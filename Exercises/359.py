# Напишіть програму, яка зчитує рядок, введений користувачем, що містить дату у формі mm/dd/yyyy.
# Програма має вивести на екран дату у вигляді Місяць Число, Рік.
# Вхідні дані:
# 12/29/2022
# 03/04/2025
# Вихідні дані:
# December 29, 2022
# March 04, 2025

# txt = input('Enter date in "mm/dd/yyyy" format: ')
txt = '04/05/1986'
list_date = txt.split('/')
list_month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
txt_date = f'{list_month[int(list_date[0])-1]} {list_date[1]}, {list_date[2]}'
print(txt_date)