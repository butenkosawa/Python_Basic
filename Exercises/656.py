# Вкладник розмістив суму розміром n грн в банку.
# Визначте, яку суму отримає вкладник через m років,
# якщо відсоткова ставка складає p% в рік.
# Дані вводяться в порядку n, p, m як у вхідних даних.
# Вхідні дані:
# 5000
# 18
# 2
# Вихідні дані:
# 6800.00

def deposit(n, p, m):
    """Визначте, яку суму отримає вкладник

    :param n: розміщенна сума, int
    :param p: відсоткова ставка, int
    :param m: кількість років, int
    :return: загальну суму без податків, str
    """
    return '{:.2f}'.format(n + n * m * p / 100)

print(deposit(5000,18,2))
