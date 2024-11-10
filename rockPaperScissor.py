import random
import sys

moveList = ['Rock', 'Paper', 'Scissors']
moveNum = [1, 2, 3]

def playFunc():
    print("Enter your choice:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    
    while True:
        try:
            playerChoice = int(input("Enter your choice: "))
            if playerChoice in moveNum:
                break
        except: 
            print("That's not a valid option, try again\n")
            continue
    
    cpuChoice = random.choice(moveNum)

    print("User choice is: ", moveList[playerChoice - 1])
    print("Computer choice is: ", moveList[cpuChoice - 1])

    if cpuChoice == playerChoice:
        print("It's a tie!")
    elif cpuChoice - playerChoice == 1 or cpuChoice - playerChoice == -2:
        print("The CPU wins!")
    else:
        print("You win!")

print("How to play: \n Rock vs Paper -> Paper wins\n Rock vs Scissors -> Rock wins \n Paper vs Scissors -> Scissors wins")

x = 0
while x == 0:
    playFunc()
    
    while True:
        try:
            replay = str(input("Do you want to play again? (Y/N)"))
            replay = replay.lower()

            if replay == 'y': 
                break
            elif replay == 'n':
                print("See ya cunt")
                x = 1
                break
        except: 
            print("Not a valid input")
            continue

sys.exit()