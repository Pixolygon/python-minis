from random import randint

play = 'y'

while play == 'y':
    random_number = randint(1,10)
    guess = int(input('Guess a number between 1 and 10: '))

    while guess != random_number:
        if guess > random_number:
            guess = int(input('Too high! Guess again: '))
        elif guess < random_number:
            guess = int(input('Too low! Guess again: '))
    play = input('You win! Play again? y/n: ')

print('Thanks for playing!')


