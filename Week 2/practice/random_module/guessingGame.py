import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

for guessTaken in range(1,7):
    print('Take a guess.')
    guessNumber = int(input())

    if guessNumber > secretNumber:
        print('Your guess is too high.')
    elif guessNumber < secretNumber:
        print("Your guess is too low.")
    else:
        break

if guessNumber == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))