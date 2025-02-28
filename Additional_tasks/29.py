# Даний список цілих чисел довжини 1 і більше. Написати функцію, яка повертає список
# довжини 2, що складається з першого та останнього елемента вхідного списку.
# [1, 2, 3] -> [1, 3], [7, 4, 6, 2] -> [7, 2], [5] -> [5, 5]

def list_two_elements(list_of_numbers: list):
    return [list_of_numbers[0], list_of_numbers[-1]]

list_1 = list_two_elements([1, 2, 3])
print(list_1)
list_2 = list_two_elements([7, 4, 6, 2])
print(list_2)
list_3 = list_two_elements([5])
print(list_3)