word = input('Enter the word:   ').split()
acronym = ''
for words in word:
    acronym += str(words[0]).upper()

print('Acronym is:  ',acronym)
