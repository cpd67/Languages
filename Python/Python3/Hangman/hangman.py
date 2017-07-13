

# WILL BE CHANGED INTO A CLASS LATER

import subprocess

# To store state...
# correctGuesses = [], where the size of the list is the length of the chosen word.
# At the start, each element will be "_"
# For each correct guess, the element which corresponds to the position in the word
# in which the letter is found will be the correct letter.
# So, if a user has the word "Hangman" and guesses the letters 'a' and 'h',
# correctGuesses would look something like:
# ["h", "a", "_", "_", "_" "a", "_"]
# and that would be printed out whenever you show the user their progress.

# Main logic:
# Loop:
#   1. Display current hangman picture.
#   2. Show word progress.
#   3. Get and check input from user.
# Three use cases to consider:
# 1. Start a new game.
#   a. Hangman picture is the noose, progress is all '_', get input as normal.
# 2. Normal gameplay.
#   a. See game logic above.
# 3. Game ends.
#   a. Either the user has guessed the word correctly, or the game is over.
#   b. If the user loses the game:
#     i. Display full Hangman picture.
#     ii. Show "Game over!"
#     iii. Ask the user if they would like to play again.
#          ai. If the user doesn't want to, exit the game.
#          bi. Else, restart the game.
#   b2. Else, if the user has guessed the word correctly:
#       i. Display "You win!"
#       ii. Ask the user if the would like to play again.
#       iii. If yes: restart the game. Else, exit the game.

# https://stackoverflow.com/questions/26236126/how-to-run-bash-command-inside-python-script
# Execute the cowsay program from a Python script
# subprocess.call(["cowsay", "hi"])

# Menu for Hangman game
def printMenu():
    print("Here are your options:")
    print("1. Play!")
    print("2. Help")
    print("3. Exit")

# Determine if user input is valid
def checkMenuInput():
    while True:
        userInput = str(input("Enter your choice: "))
        if userInput not in ("1", "2", "3"):
            print("Invalid input!")
            printMenu()
        elif userInput == "1":
            print("Start!")
            break
        elif userInput == "2":
            print("Help!")
            break
        elif userInput == "3":
            print("Exit!")
            break

# Play the actual game
def playGame():

    #http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
    # Read a word from the text file
    fileHandler = open("./words.txt", "r")

    # Read the first word of the word.txt file
    # TODO: Replace this with reading a random word from the text file.
    word = fileHandler.readline()

    fileHandler.close()

    # Number of guesses that the player has accumulated.
    numGuesses = 0

    # Inspiration obtained from: https://stackoverflow.com/questions/18098326/dynamically-declare-create-lists-in-python
    # Use a list comp to create a list of blanks
    # based off the size of the chosen word.
    # (WILL BE MOVED INTO A FUNCTION LATER)
    correctGuesses = ["_" for n in range((len(word))) ]

    for i in correctGuesses:
        print(i, end=" ")

    print("\n")

    while numGuesses < 6:
        # Show the first hangman picture.
        subprocess.call(["cat", "./Drawings/hangman0.txt"])

        # Get input
        x = str(input("Enter a letter: "))
        # If letter was in the word
        if x in word:
            # Display letters
            print("You got one letter right!")
        else:
            # Increment number of guesses, show hangman drawing
            print("Damn it! That's wrong!")
            numGuesses = numGuesses + 1
            subprocess.call(["cat", "./Drawings/hangman" + str(numGuesses) + ".txt"])

def showHelp():
    pass

# Will be used to show the progress of the user
def showProgress():
    for i in correctGuesses:
        print(i, end="")
        if i == len(correctGuesses):
            print("\n")

if __name__ == "__main__":
    print("Running hangman tests...")
    # Test 1: Printing the menu.
    printMenu()
    # Test 2: Checking user input.
    checkMenuInput()
    # Test 3a: Testing main game loop logic, part 1.
    playGame()
