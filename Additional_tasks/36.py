# Напишіть програму, яка створює словник, що містить інформацію про
# студентів та їх оцінки. Ключами словника є імена студентів, а
# значеннями – списки оцінок. Створіть функцію calculate_average_grade,
# яка приймає словник з оцінками студентів та обчислює середній бал
# для кожного студента. Функція повинна повертати новий словник, у
# якому ключами є імена студентів, а значеннями - їх середній бал.
# Виведіть результат на екран.
#
# Приклад словника з оцінками
# grades = {
# 'Alice': [85, 90, 92],
# 'Bob': [78, 80, 84],
# 'Carol': [92, 88, 95]
# }
#
# Приклад висновку:
# {'Alice': 89.0, 'Bob': 80.67, 'Carol': 91.67}

def calculate_average_grade(students_grades: dict) -> dict:
    average_grade = {}
    for key, value in students_grades.items():
        average_grade[key] = round(sum(value) / len(value), 2)
    return average_grade

grades = {'Alice': [85, 90, 92], 'Bob': [78, 80, 84], 'Carol': [92, 88, 95]}
print(calculate_average_grade(grades))

# Рішення викладача:

def calculate_average_grade(x):
    k = {}
    for key, value in x.items():
        k[key] = round(sum(value) / len(value), 2)
    return k


grades = {'Alice': [85, 90, 92], 'Bob': [78, 80, 84], 'Carol': [92, 88, 95]}
print(calculate_average_grade(grades))

