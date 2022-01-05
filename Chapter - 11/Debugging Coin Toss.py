import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
print(toss,guess)
if ((toss==0 and guess=='tails') or (toss==1 and guess=='heads')):
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if ((toss==0 and guesss=='tails') or (toss==1 and guesss=='heads')):
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
