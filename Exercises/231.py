# Пароль доступу до комп’ютера зберігається у змінній n - ціле число, яке вводить користувач.
# Напишіть програму, яка запитує пароль в користувача. У разі введення користувачем неправильного пароля
# на екран має виводитися повідомлення Error, після чого дії повинні повторюватися до введення правильного значення.
# При успішній аутентифікації в ситемі має з’явитися повідомлення Done.

n = 12345
password = int(input("Enter password: "))

while password != n:
    print("Error")
    password = int(input("Enter password: "))
    if password == n:
        print("Done")

