# Дано натуральне число N. Написати функцію power_of_2(N), яка друкує
# слово YES, якщо число N є точним ступенем двійки, або слово NO в
# інакше. Користуємося рекурсією, а операцією зведення на ступінь не
# користуємося.
#
# Приклад:
# power_of_2(8) поверне YES
# poser_of_2(3) поверне NO.


def power_of_2(n):
    return "YES" if n & n - 1 == 0 else "NO"

for i in range(1, 21):
    print(i, power_of_2(i))


# Рішення викладача:

def power_of_2(N):
    if N == 1:
        return True
    elif N % 2 != 0 or N == 0:
        return False
    else:
        return power_of_2(N // 2)


print(power_of_2(16))