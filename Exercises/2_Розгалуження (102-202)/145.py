# Квадратне рівняння

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

x1 = None
x2 = None
D = b ** 2 - 4 * a * c

if D > 0:
    x1 = round((-b + D ** 0.5) / (2 * a), 2)
    x2 = round((-b - D ** 0.5) / (2 * a), 2)
    print(x1, 'and', x2)
elif D == 0:
    x1 = round((-b / (2 * a)), 2)
    print(x1)
else:
    print('No roots')
