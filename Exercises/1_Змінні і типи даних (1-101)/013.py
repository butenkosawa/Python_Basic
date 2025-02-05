# Площа круга та довжина кола
r = float(input("Введіть радіус кола: "))
from math import pi
PI = round(pi, 2)

s = PI * r ** 2
l = 2 * PI * r

print(PI)
print("Площа круга ->", f"{s:.{3}f}")
print("Довжина кола ->", f"{l:.{3}f}")
