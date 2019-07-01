import random

print('---------------------------------')
print(' JOHANNES GUESS THAT PRIMER GAME')
print('---------------------------------')
print()

goal = random.choice('ACGT')
goal += random.choice('ACGT')
goal += random.choice('ACGT')
goal += random.choice('ACGT')
goal += random.choice('ACGT')


guess = 'NNNNN'

name = input('Player what is your name? ')

while guess != goal:
    guess = input('Guess a 5 bp primer: ')

    misses = 0
    for i in range(len(guess)):
        if guess[i] != goal[i]:
            misses += 1
    if misses > 0:
        print('Sorry, you have %i misses. Lets play again!' % misses)

    else:
        print('Excellent {}, you won!'.format(name))
print('done')
