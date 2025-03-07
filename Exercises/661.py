# На стадіоні є три категорії місць для сидіння: місця класу A коштують a грошових одиниць,
# місця класу B коштують b грошових одиниць, а місця класу C - c грошових одиниць.
# Напишіть першу функцію, яка запитує скільки продано квитків на кожний клас місць,
# і другу функцію, яка відображає суму отриманого доходу від продажу квитків на кожен
# клас окремо і загалом. Формати введення і виведення такі, як у вхідних і вихідних даних.
# Вхідні дані:
# A
# 20.50
# 45
# B
# 15.75
# 30
# C
# 10.55
# 15
# Вихідні дані:
# ({'A': 922.5, 'B': 472.5, 'C': 158.25}, 1553.25)
from copy import deepcopy
from collections import defaultdict


def tickets_sold():
    tickets = dict.fromkeys(('A', 'B', 'C'))
    for key in tickets:
        tickets[key] = int(input(f'Enter the number of tickets sold for class "{key}" seats: '))
    return tickets

def amount_of_income(A, B, C, tickets_class:dict):
    price = (A, B, C)
    tickets_price = dict(zip(tickets_class.keys(), price))
    income_class = {key: tickets_class[key] * tickets_price[key]
                    for key in tickets_class}
    income = sum(income_class.values())


    return income_class, income


tickets = tickets_sold()
print(amount_of_income(20.50, 15.75, 10.55, tickets))