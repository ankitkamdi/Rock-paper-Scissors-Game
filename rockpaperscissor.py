from random import randint
'''I used this module for generating random
                              inputs from computer for the game'''


#I have created  a list of playing  options for computer
t = ["Rock","Paper", "Scissors"]

#Assigning  a random choices to the computer using list 
computer = t[randint(0,2)]

#set player to False               
player = False

                         
while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if(player == computer):
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
    # Finally we reset the player value to False to restart the while loop.
