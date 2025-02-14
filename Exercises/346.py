# Напишіть програму, щоб отримати рядок із введеного користувачем рядка,
# де всі входження першого символа у рядку змінилися на рядок *HIDE*, за винятком першого.
# Вхідні дані:
# Endless clouds drifted back and forth, blotting out the RED SUN
# Вихідні дані:
# Endl*HIDE*ss clouds drift*HIDE*d back and forth, blotting out th*HIDE* R*HIDE*D SUN

txt = input('Enter any text: ')
# txt = 'Endless clouds drifted back and forth, blotting out the RED SUN'
txt_hide = txt[0] + txt.replace(txt[0].lower(), txt[0].upper())[1:].replace(txt[0].upper(), '*HIDE*')
print (txt_hide)
