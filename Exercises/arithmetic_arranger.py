def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        raise ValueError('Error: Too many problems.')
    elif '*' in "".join(problems) or '/' in "".join(problems):
        raise ValueError("Error: Operator must be '+' or '-'.")
    elif not only_numbers(problems):
        raise ValueError('Error: Numbers must only contain digits.')
    elif check_len_operands(problems):
        raise ValueError('Error: Numbers cannot be more than four digits.')

    first_operands = []
    operators = []
    second_operands = []
    len_problem = []
    solutions = []

    for problem in problems:
        el = problem.split()
        first_operands.append(el[0])
        operators.append(el[1])
        second_operands.append(el[-1])

    for i in range(len(operators)):
        if operators[i] == '+':
            solutions.append(str(int(first_operands[i]) + int(second_operands[i])))
        else:
            solutions.append(str(int(first_operands[i]) - int(second_operands[i])))

    for i in range(len(first_operands)):
        len_problem.append(max([len(first_operands[i]), len(second_operands[i])]) + 2)

    for i in range(len(first_operands)):
        first_operands[i] = first_operands[i].rjust(len_problem[i]) + ' ' * 2

    row_1 = ''.join(first_operands)[:-2]

    for i in range(len(second_operands)):
        second_operands[i] = operators[i] + second_operands[i].rjust(len_problem[i] - 1) + ' ' * 2

    row_2 = ''.join(second_operands)[:-2]

    for i in range(len(solutions)):
        solutions[i] = solutions[i].rjust(len_problem[i]) + ' ' * 2

    row_4 = ''.join(solutions)[:-2]

    for i in range(len(len_problem)):
        len_problem[i] = "-" * len_problem[i] + ' ' * 2

    row_3 = ''.join(len_problem)[:-2]

    if show_answers is True:
        return row_1 + '\n' + row_2 + '\n' + row_3 + '\n' + row_4
    return row_1 + '\n' + row_2 + '\n' + row_3

def only_numbers(problems):
    problems_string = ''.join(problems)
    return (problems_string.replace("+", "").replace("-", "").
            replace(" ", "").isdigit())


def check_len_operands(problems):
    for el in problems:
        for num in list(filter(lambda x: x not in ('+', '-'), list(el.split()))):
            if len(num) > 4:
                return True


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print("*" * 30)
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))