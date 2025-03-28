# Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач
# цього хоче. Тобто, потрібно робити запит до користувача на продовження
# роботи калькулятора після кожного обчислення - якщо користувач ввів yes
# (можна просто y), то нове обчислення, інакше - закінчення роботи.

while True:
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

    ask = str(input('Enter "yes" or "y" if you want to continue, else press the "Enter" key: '))
    if ask.upper() not in ["YES", "Y"]:
        break

# Рішення викладача

while True:
    first_number = int(input("input the first number: "))
    second_number = int(input("input the second number: "))
    action = input("input the sign for calculation action: ")

    if action == "+":
        print("a + b =", first_number + second_number)
    elif action == "-":
        print("a - b =", first_number - second_number)
    elif action == "*":
        print("a * b =", first_number * second_number)
    elif action == "/":
        if second_number == 0:
            print("The denominator can't be 0. Calculation can't be done")
        else:
            print("a / b =", first_number / second_number)
    else:
        print("Please choose one of the following simbols for calculation: +, -, *, /")

    answer = input("Do you want continue? (yes/y)").lower()
    if answer not in ('yes', 'y'):
        break