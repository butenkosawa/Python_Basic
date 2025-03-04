# Напишіть функцію, яка отримує 3 аргументи: перші 2 - числа, третій - операція (+, -, *, /),
# яка повинна бути проведена над ними. У випадку невідомої операції, функція повертає рядок Unknown operation.
# Результатом має бути дійсне число з двома знаками після десяткової крапки.
# Вхідні дані:
# 3
# 8
# +
# Вихідні дані:
# 11.00

def calculate(num1, num2, operand):
    if operand == "+":
        return '{:.2f}'.format(num1 + num2)
    elif operand == "-":
        return '{:.2f}'.format(num1 - num2)
    elif operand == "*":
        return '{:.2f}'.format(num1 * num2)
    elif operand == "/":
        return '{:.2f}'.format(num1 / num2)
    else:
        return 'Unknown operation.'


print(calculate(3, 8, '+'))
print(calculate(3, 8, '-'))
print(calculate(3, 8, '*'))
print(calculate(3, 8, '/'))
print(calculate(3, 8, '%'))
