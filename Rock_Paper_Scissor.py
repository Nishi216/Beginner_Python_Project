import random
choices = ['Rock','Paper','Scissor']
computer = random.choice(choices)

player = False
computer_score=0
player_score=0

while True:
    player = input('Rock , Paper or Scissor? (End to end the game)').capitalize()
    if player == computer:
        print('Tie')
        computer = random.choice(choices)
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose')
            computer_score += 1
            computer = random.choice(choices)
        else:
            print('You Win')
            player_score += 1
            computer = random.choice(choices)
    elif player == 'Paper':
        if computer == 'Scissor':
            print('You lose')
            computer_score += 1
            computer = random.choice(choices)
        else:
            print('You Win')
            player_score += 1
            computer = random.choice(choices)
    elif player == 'Scissor':
        if computer == 'Rock':
            print('You lose')
            computer_score += 1
            computer = random.choice(choices)
        else:
            print('You Win')
            player_score += 1
            computer = random.choice(choices)
    elif player == 'End':
        print('Final scores:  computer is {} and player is {}'.format(computer_score,player_score))
        if player_score>computer_score:
            print('You win the match')
        else:
            print('Computer won the match')
        break