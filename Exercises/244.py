# Надрукувати усі двоцифрові числа, сума квадратів цифр яких ділиться на n націло.
# Число n - ціле число, яке вводить користувач.

# n = int(input("Enter number, n: "))
n = 9
num1 = None
num2 = None

for number in range(10, 100):
    num1, num2 = divmod(number, 10)
    if (num1 ** 2 + num2 ** 2) % n == 0:
        print(number, end=' ')
