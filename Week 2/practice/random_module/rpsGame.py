import random, sys
wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')

while True:
    print(wins, 'Wins', losses, 'Losses', ties, 'Ties')
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        choice = input()

        if choice == 'q':
            sys.exit() #quit the program
        if choice == 'rock' or choice == 'paper' or choice == 'scissors':
            break
        print('Type one of r, p, s, or q.')

    #Dispay what computer choose
    randomNumber = random.randint(1,3)

    if randomNumber == 1:
        computerMove = 'rock'
    elif randomNumber == 2:
        computerMove = 'paper'
    elif randomNumber == 3:
        computerMove = 'scissors'

    #Displays what player choose

    if choice == 'rock':
        print('ROCK vs.', computerMove.upper())
    elif choice == 'paper':
        print('PAPER vs.', computerMove.upper())
    elif choice == 'scissors':
        print('SCISSORS vs.', computerMove.upper())

    #Display and record the Win/Loss/Tie

    if choice == computerMove:
        print("It's a tie!")
        ties += 1

    # Wins
    elif choice == 'rock' and computerMove == 'scissors':
        print('You win!')
        wins += 1
    elif choice == 'paper' and computerMove == 'rock':         
        print('You win!')         
        wins = wins + 1     
    elif choice == 'scissors' and computerMove == 'paper':         
        print('You win!')         
        wins = wins + 1

    # Losses     
    elif choice == 'rock' and computerMove == 'paper':         
        print('You lose!')         
        losses = losses + 1     
    elif choice == 'paper' and computerMove == 'scissors':         
        print('You lose!')         
        losses = losses + 1     
    elif choice == 'scissors' and computerMove == 'rock':         
        print('You lose!')         
        losses = losses + 1

'''
This program uses a while loop inside of another while loop. 
The first loop is the main game loop, and a single game of rock, paper,
scissors is player on each iteration through this loop. The second loop asks for 
input from  the player, and keeps looping until the player has entered an r, p, s,
or q for their move. The r, p, and s correspond to rock, paper, and scissors, 
respectively, while the q means the player intends to quit. 
In that case, sys.exit() is called and the program exits.
'''