import random

print('---------------------------------')
print(' JOHANNES GUESS THAT NUMBER GAME')
print('---------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        # print('Your guess of ' + guess + ' was too LOW.')
        print('Sorry {}, your guess of {} was just a bit too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH, man!'.format(name, guess))
    else:
        print('Excellent {}, you won, it was {}!'.format(name, guess))

print('done')
