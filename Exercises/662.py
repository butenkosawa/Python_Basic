# Напишіть функцію, яка отримує послідовність балів (цілі числа)
# і повертає буквенну інтерпретацію числових балів на основі наступної шкали оцінок:
# 90-100 - A
# 80-89 - B
# 70-79 - C
# 60-69 - D
# Нижче 60 - F
# Вхідні дані:
# 60 80 64 45 35 87 90 95 91 64 78
# Вихідні дані:
# {'A': [90, 95, 91], 'B': [80, 87], 'C': [78], 'D': [60, 64, 64], 'F': [45, 35]}

def grades(*args):
    grades_dict = {'A': [], 'B': [], 'C': [], 'D': [], 'F': []}

    for grade in args:
        if 90 <= grade <= 100:
            grades_dict['A'].append(grade)
        elif grade >= 80:
            grades_dict['B'].append(grade)
        elif grade >= 70:
            grades_dict['C'].append(grade)
        elif grade >= 60:
            grades_dict['D'].append(grade)
        else:
            grades_dict['F'].append(grade)
    return grades_dict

print(grades(60, 80, 64, 45, 35, 87, 90, 95, 91, 64, 78))