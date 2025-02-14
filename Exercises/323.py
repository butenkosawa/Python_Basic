# Напишіть програму, щоб перевірити, з яких символів складається рядок, введений користувачем:
# лише з цифр, лише з букв, або з букв і цифр.

txt = input('Enter any text: ')

if txt.replace(' ', '').isdigit():
    print('Your message includes numbers only.')
elif txt.replace(' ', '').isalpha():
    print('Your message includes letters only.')
elif txt.replace(' ', '').isalnum():
    print('Your message includes numbers and letters.')
else:
    print('Your message includes special symbols.')