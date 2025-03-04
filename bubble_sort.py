def bubble_sort(arr):
    n = len(arr) # 7
    # print(arr)
    # print('-' * 30)
    for i in range(n - 1): # [0, 1, 2, 3, 4, 5]
        for j in range(0, n - i - 1):
            # Цикл 1: [0, 1, 2, 3, 4]
            # Цикл 2: [0, 1, 2, 3]
            # Цикл 3: [0, 1, 2]
            # Цикл 4: [0, 1]
            # Цикл 4: [0]
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # print(arr)

# Приклад використання
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Відсортований масив:", my_list)