# Написати функцію, яка повертає true, якщо у списку йде поспіль два
# рази задане число.
# Якщо задане число 2, то [1, 2, 2, 8] -> true, [2, 1, 2] -> false

def two_elements(list_of_numbers: list):
    for i in range(len(list_of_numbers)-1):
        if list_of_numbers[i] == list_of_numbers[i+1]:
            return True
        else:
            continue
    return False


print(two_elements([1, 2, 2, 8]))