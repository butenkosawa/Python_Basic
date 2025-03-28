# Розділити один список на два списки

lst_0 = [1, 99, 3, True, "Hello", 3.5, 0]
# lst_0 = ['Bob', 'Mike', False, 10]
# lst_0 = []

half_len = round(len(lst_0) / 2 + 0.1)

lst_1 = lst_0[:half_len]
lst_2 = lst_0[half_len:]
lst_res = [lst_1, lst_2]

print(lst_0)
print(lst_res)

# Рішення викладача

input_list = [56, 78, 20]

mid = (len(input_list) + 1) // 2

first_half = input_list[:mid]
second_half = input_list[mid:]

print(input_list, "=>", [first_half, second_half])
