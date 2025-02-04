# Визначте назву геометричної фігури за введеною кількістю її сторін.
# Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін
# поза межами цього діапазону, програма повинна відображати відповідне повідомлення.

n = int(input("Enter the number of sides of the shape: "))

if n == 3:
    print('That\'s a triangle.')
elif n == 4:
    print('That\'s a quadrilateral.')
elif n == 5:
    print('That\'s a pentagon.')
elif n == 6:
    print('That\'s a hexagon.')
else:
    if n < 3 or n >6:
        print('That number of sides is not supported by this program.')
