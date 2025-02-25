# Напишіть програму, яка запитує у користувача суму у євро і потім виводить:
# мінімальну кількисть купюр та мінімальну кількість монет для того, щоб
# отримати цю суму у євро. Зверніть увагу на те, що банкноти євро мають
# номінали: 5, 10, 20, 50, 100, 200 та 500 евро. А монети: 1 та 2 євро,
# 1, 2, 5, 10, 20 та 50 євроцентів.
# Крім того треба надрукувати кількість кожного номіналу котрий
# використовується для отримання даної суми.
# * Бажано, щоб суму можна було вводити як через крапку так і через кому.
from collections import defaultdict

# Приклад: Введіть суму: 347,78
# Кількість банкнот: 5
# Кількість монет: 7
# Склад суми:
# 1 x 200
# 1 x 100
# 2 x 20
# 1 x 5
# 2 x 1
# 1 x 0.5
# 1 x 0.2
# 1 x 0.05
# 1 x 0.02
# 1 x 0.01

cash = input("Введіть суму у євро: ")
if "," in cash:
    cash = cash.replace(",", ".")
cash = float(cash)

banknotes_nominal = (500, 200, 100, 50, 20, 10, 5)
coins_nominal = (2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01)
banknotes = defaultdict()
coins = defaultdict()

for nominal in banknotes_nominal:
    if nominal > cash:
        continue
    number, cash = divmod(cash, nominal)
    banknotes[nominal] = int(number)

for nominal in coins_nominal:
    if nominal > cash:
        continue
    number, cash = divmod(cash, nominal)
    cash = round(cash, 2)
    coins[nominal] = int(number)

print(f"Кількість банкнот {sum(banknotes.values())}")
for k, v in banknotes.items():
    print(f"{v} x {k}")

print(f"Кількість монет {sum(coins.values())}")
for k, v in coins.items():
    print(f"{v} x {k}")