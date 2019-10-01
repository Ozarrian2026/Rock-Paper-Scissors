# Ozarrian John
#Rock, Paper, Scissors Game
#_______________________________________________________________________________________________
# break into pieces
# welcome page, with name entry
# Score screen with computer, player(name), ties
# Options for game r, p, s, q 
# Game will loop until q is entered
# Each loop it will get a random choice from the computer
# a choice from the player, compare the two, and update the score
# when the game is over(q is entered) final score is displayed

# WELCOME PAGE
# prompt for the player name
# a welcome message

#_______________________________________________________________________________________________________

# imports
import random
# variables
playerScore = 0
computerScore = 0
ties = 0
# make a list
cChoices =["r", "p", "s"]
print("Welcome to Rock Paper Scissors")
name = input("Enter your name: ")
# main loop
while True:
	# print score
	print("Score:")
	print("Computer:" + str(computerScore))
	print(name + ":" + str(playerScore))
	print("Ties:" + str(ties))
	choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' for quit:")
	computerChoice = random.choice(cChoices)
	if choice == "q":
		print("Thanks for playing!")
		break

	if choice == "r":
		print(name + " picked rock")
		if computerChoice == "r":
			print("Computer picked Rock")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "p":
			print("Computer picked Paper")
			print("Paper beats Rocks")
			computerScore += 1
		else: # s is only choice left
		    print("Computer picked Scissors")
		    print("Rocks beats Scissors")
		    playerScore += 1
	elif choice == "p":
		print(name + " picked paper")
		if computerChoice == "p":
			print("Computer picked paper")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "s":
			print("Computer picked Scissors")
			print("Scissors beats paper")
			computerScore += 1
		else:
			print("Computer picked Rock")
			print("Paper beats Rock")
			playerScore += 1
	elif choice == "s":
		print(name + " picked scissors")
		if computerChoice == "s":
			print("Computerpicked scissors")
			print("This is a tie")
			ties = ties + 1
		elif computerChoice == "r":
			print("Computer picked rock")
			print("Rock beats Scissors")
			computerScore += 1
		else:
			print("Computer picked paper")
			print("Scissors beats Paper")
			playerScore += 1


	else:
		print("This is not an option, choose the given options")