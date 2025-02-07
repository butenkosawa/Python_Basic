# Вводяться координати (x, y) точки A і радіус кола (r).
# Визначити, чи належить дана точка колу, якщо його центр знаходиться в початку координат.

x = float(input('Enter x coordinate: '))
y = float(input('Enter y coordinate: '))
r = float(input('Enter circle radius: '))

if x**2 + y ** 2 == r ** 2:
    print('The point belongs to the circle')
else:
    print('The point is outside the circle')
