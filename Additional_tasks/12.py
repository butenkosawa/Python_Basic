# Напишіть програму, яка приймає число з плаваючою точкою і округляє його до
# цілого числа відповідно до правил шкільної математики. Використовувати
# модуль math та методи з нього не можна. Врахувати, що програма має коректно
# працювати з негативними числами.
#
# Приклад:
# Введіть дійсне число: -3.14
# Округлене значення: -3
# Введіть дійсне число: 4.5
# Округлене значення: 5
# Введіть дійсне число: 5.5
# Округлене значення: 6

n = float(input("Enter number: "))
n = n + 0.01 if n > 0 else n - 0.01
print(round(n))