import random
import time
# return 0 for user wins
# return 1 for computer wins
# return -1 for tie
def whoWins(userChoice, computerChoice):
    if userChoice == computerChoice:
        return -1
    if userChoice == 0 and computerChoice == 1:
        return 1
    if userChoice == 0 and computerChoice == 2:
        return 0
    if userChoice == 1 and computerChoice == 0:
        return 0
    if userChoice == 1 and computerChoice == 2:
        return 1
    if userChoice == 2 and computerChoice == 0:
        return 1
    if userChoice == 2 and computerChoice == 1:
        return 0
def numberToString(num):
    if num == 0:
        return "rock"
    if num == 1:
        return "paper"
    if num == 2:
        return "scissors"
def stringToNumber(input):
    if input.lower() == "rock":
        return 0
    if input.lower() == "paper":
        return 1
    if input.lower() == "scissors":
        return 2
    if input.lower() == "exit":
        exit()
    else:
        return -1
nUserWins = 0
nComputerWins = 0
nRounds = int(input("How many rounds do you want to play?  "))
if nRounds <= 0 or nRounds >= 100:
    print("Not a valid number of rounds. Has to be between 0 and 99.")
    exit()
for i in range(0, nRounds):
    print("\nROUND " + str(i+1) + " OUT OF " + str(nRounds))
    while True:
        userChoice = stringToNumber(input("Rock, paper, or scissors? (type exit to exit) "))
        if userChoice != -1:
            break
        print("Not valid choice. You have to pick rock, paper, scissors, or exit")
    n = random.randint(0, 100)
    if n >= 0 and n <= 50:
        computerChoice = 0
    if n > 50 and n <= 75:
        computerChoice = 1
    if n > 75:
        computerChoice = 2
    time.sleep(1)
    print("PC chose " + numberToString(computerChoice))
    winner = whoWins(userChoice, computerChoice)
    if winner == 0:
        print("You win")
        nUserWins += 1
    if winner == 1:
        print("Sorry, you lose")
        nComputerWins += 1
    if winner == -1:
        print("Tie")
    print("So far, you have " + str(nUserWins) + " wins. PC has " + str(nComputerWins) + " wins.")
if nUserWins > nComputerWins:
    print("Out of the " + str(nRounds) + " games, you win")
if nUserWins < nComputerWins:
    print("Out of the " + str(nRounds) + " games, you lose")
if nUserWins == nComputerWins:
    print("Out of the " + str(nRounds) + " games, you tied")