# Rock Paper Scissor
#   By Cameron Gerossie (Sunday, September 12, 2021)

from random import randint

choice = ["rock", "paper", "scissors"]

same = True
count = 0
cGuess = 0
uGuess = 0

while same:
    cGuess = randint(0,2)
    print("Computer Guess:", choice[cGuess])

    uGuess = input("Enter a chocie (0 = rock, 1 = paper, 2 = scissors): ")
    uGuess = int(uGuess)

    if uGuess != cGuess:
        same = False
    else:
        print("Same Choice, Try Again.")

print("Computer Guessed:", choice[cGuess])
print("User Guess:", choice[uGuess])


if(uGuess == 0): # if user guess is rock
    if cGuess == 1:
        win = False # Rock vs Paper - Lose
    if cGuess == 2:
        win = True # Rock vs Scissors - Win

if(uGuess == 1): # if user guess is paper
    if cGuess == 0:
        win = True # Paper vs Rock - Win
    if cGuess == 2:
        win = False # Paper vs Scissors - Lose


if(uGuess == 2): # if user guess is scissors
    if cGuess == 1:
        win = True # Scissors vs Paper - Win
    if cGuess == 0:
        win = False # Scissors vs Rock - Lose

if win:
    print("You win", choice[uGuess], "beats", choice[cGuess])
else:
    print("You lose", choice[uGuess], "is beat by", choice[cGuess])
