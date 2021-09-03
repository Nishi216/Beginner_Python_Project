import random
import math

low = int(input('Enter the lower number:  '))
high = int(input('Enter the higher number:  '))

rand_num = random.randint(low,high)
min_guess = math.log(high-low+1,2)
print('You have ',round(min_guess),' guesses left')

count=0
while count<min_guess:
    count += 1
    guess = int(input('Enter your guess:   '))
    if guess==rand_num:
        print('Congratulations! You have guessed the number, that is ',rand_num)
        print('You guessed the number in ',count,' attempt')
        break
    elif guess>rand_num:
        print('Your guess ',guess,' is high.')
    elif guess<rand_num:
        print('Your guess ',guess,' is low.')

if count>min_guess:
    print('The number to be guessed was:  ',rand_num)
    print('Better luck next time.')

