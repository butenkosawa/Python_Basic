# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
# 1) ніяких символів з набору string.punctuation не повинно бути, у тому
#    числі й пробілів;
# 2) підсумкова довжина hashtag має бути не більше 140 символів.
# 3) кожне слово починається з великої літери.
# 4) якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.
#
# Приклади:
# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I. subscribe? Yes!' -> #ShouldISubscribeYes

from string import punctuation

text = input('Enter any text: ')
list_text = list(text.title().replace(' ',''))
clean_list_text = [sym for sym in list_text if sym not in punctuation]
clean_list_text.insert(0, '#')

print(''.join(clean_list_text)[:140])

# Рішення викладача

punctuation_symbols = r''' !"#$%&'()*+,-./:;<=>?@[\]_^`{|}~'''
punctuation_symbols_list = [i for i in punctuation_symbols]

user_variable = input('Input your sentence: ').title()
hashtag = "#" + ''.join([i for i in user_variable if i not in punctuation_symbols_list])

if len(hashtag) > 140:
    hashtag = hashtag[0:140]

print(f'The hashtag is created: {hashtag}')