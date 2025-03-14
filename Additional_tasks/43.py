# Створіть клас BankAccount для надання банківського рахунку. Клас повинен
# мати атрибути account_number (номер рахунку) та balance (баланс), а також
# методи deposit() для внесення грошей на рахунок і withdraw() для зняття
# грошей з рахунку. Потім створіть екземпляр класу BankAccount, внесіть на
# рахунок деяку суму і зніміть частину грошей. Виведіть баланс, що залишився.
# Не забудьте передбачити варіант, при якому при знятті баланс може стати
# меншим за нуль. У цьому випадку йти в мінус не будемо, замість чого
# повертатимемо повідомлення "Недостатньо коштів на рахунку".

class BankAccount:

    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
         return self.balance - money if self.balance > money else 'Недостатньо коштів на рахунку'

ba = BankAccount('4444 1111 2525 7548')
ba.deposit(1000)
print(ba.balance)
print(ba.withdraw(521))
print(ba.withdraw(1521))


