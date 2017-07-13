
import subprocess

# Global for the number of guesses that the player has accumulated.
numGuesses = 0

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
    # TODO: Replace with an I/O call to read a random word from a text file.
    word = "Test"

    while numGuesses < 7:
        # Show drawing:
        subprocess.call(["cat", "./Drawing/hangman" + str(numGuesses) + ".txt"])
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
    # 1. Read a random word from a text file.
    # 2. Display the first hangman.
    # 3. For each letter in the word:
    #     3a. Show '_ '
    # 4. While the user hasn't guessed 7 times:
    #     4a. Show the letters of the alphabet.
    #     4b. Ask the user for input.
    #     4c. Check the input:
    #         4d. If the input is a letter of the word:
    #             4da. Loop through the word and print out the letter in the
    #                  corresponding spots.
    #             Else:
    #             Print next hangman picture.

def showHelp():
    pass

if __name__ == "__main__":
    print("Running hangman tests...")
    # Test 1: Printing the menu.
    printMenu()
    # Test 2: Checking user input.
    checkMenuInput()
    # Test 3a: Testing main game loop logic, part 1.
    playGame()
