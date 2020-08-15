string = input('Введите слова через пробел: ')
wordList = string.split()
count = 0

print('Количество слов: ', len(wordList))

for word in wordList:
    if word.find('r') != -1:
        count += 1

print('Слов с буквой 'r':', count)
