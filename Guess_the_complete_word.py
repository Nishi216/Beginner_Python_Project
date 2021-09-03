import random

name = input('Enter your name:   ')
print('Good Luck ! ',name)

words = ['rainbow','computer','python','art','music','coding',
         'reverse','water','games','player','condition','chess']

word_selected = random.choice(words)
turns = int(input('Enter the maximum number of turns to use for guessing : '))

print('Guess the characters : ')
guesses=''

while turns>0:
    fail = 0
    for char in word_selected:
        if char in guesses:
            print(char)
        else:
            print('_')
            fail +=1
    if fail==0:
        print('You win!')
        print('The word is:  ',word_selected)
        print('You found it in ',turns,' guesses')
        break

    guess = input('Guess a character:  ')
    guesses+=guess
    if guess not in word_selected:
        turns-=1
        print('Wrong')
        print('You have ',turns,' left to guess')
        if turns ==0:
            print('You Loose')