from string import punctuation

text = input('Enter any text: ')
list_text = list(text.title().replace(' ',''))
clean_list_text = [sym for sym in list_text if sym not in punctuation]
clean_list_text.insert(0, '#')

print(''.join(clean_list_text)[:140])
