# Напишіть програму-таймер зворотного відліку, яка запитує у користувача
# кількість секунд n, з якої слід починати відлік.

start_time = int(input("At what second should the countdown begin?: "))

for i in range (0, start_time):
    print(start_time)
    start_time -= 1

print("Start!")
