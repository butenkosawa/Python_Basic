# Географ хоче знаходити відстань між двома точками на карті. Напишіть для
# нього програму, яка запитує у користувача координати двох точок у
# двовимірному просторі (x1, y1) та (x2, y2), а потім обчислює та виводить
# відстань між цими точками за формулою:
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

# де sqrt – функція вилучення квадратного кореня. Не використовуйте вбудовану
# математичну функцію sqrt для обчислення кореня. Не забувайте, що
# sqrt(x)==x**0.5. Результат слід вивести за допомогою команди print.

# Приклад:
# Введіть координати першої точки (x1, y1): 2, 3
# Введіть координати другої точки (x2, y2): 5, 7

# Відстань між точками: 5.0

point1 = list(input('Введіть координати першої точки (x1, y1): ').replace(' ', '').split(','))
point2 = list(input('Введіть координати першої точки (x2, y2): ').replace(' ', '').split(','))
print('Відстань між точками:', ((float(point2[0]) - float(point1[0])) ** 2 + (float(point2[1]) - float(point1[1])) ** 2) ** 0.5)