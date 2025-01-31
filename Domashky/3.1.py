# Найпростіший калькулятор

num_1 = input('Enter first number: ')
num_2 = input('Enter second number: ')
action = input('Enter action symbol (+ add, - subtract, * multiply, / divide): ')

if action == '+':
    result = float(num_1) + float(num_2)
elif action == '-':
    result = float(num_1) - float(num_2)
elif action == '*':
    result = float(num_1) * float(num_2)
else:
    if float(num_2) == 0:
        result = 'Division by 0 is not possible.'
    else:
        result = float(num_1) / float(num_2)

print(result)
