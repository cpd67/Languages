

# TODO: Make game code more efficient...

import subprocess
import linecache
import random

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

class Hangman:

    # Class variables go here...

    # Constructor for the Hangman class
    def __init__(self):
        # Instance variables...
        self.correctGuesses = []
        self.chosenWord = ""
        self.fileSizeByLines = 0
        self.numWrongGuesses = 0

    # Get file size, choose random word, etc...
    def setup(self):

        randNum = 0

        # https://stackoverflow.com/questions/19001402/how-to-count-the-total-number-of-lines-in-a-text-file-using-python
        # https://docs.python.org/3.3/tutorial/inputoutput.html
        # The 'with' keyword has the advantage that the file is properly closed after its suite is finished.
        with open('./words.txt', 'r') as fileHandler:
            # Get the number of lines currently in the text file.
            self.fileSizeByLines = sum(1 for x in fileHandler)

        randNum = random.randrange(1, self.fileSizeByLines)

        # https://docs.python.org/3/library/linecache.html#module-linecache
        # Get random word from the text file.
        self.chosenWord = linecache.getline('./words.txt', randNum)

        # Inspiration obtained from: https://stackoverflow.com/questions/18098326/dynamically-declare-create-lists-in-python
        # Use a list comp to create a list of blanks
        # based off the size of the chosen word.
        self.correctGuesses = ["_" for n in range((len(self.chosenWord)-1))]

    # Menu for Hangman game
    def printMenu(self):
        print("Here are your options:")
        print("1. Play!")
        print("2. Help")
        print("3. Exit")
        self.checkMenuInput()

    # Determine if user input at menu is valid
    def checkMenuInput(self):
        while True:
            userInput = str(input("Enter your choice: "))
            if userInput not in ("1", "2", "3"):
                print("Invalid input!")
                self.printMenu()
            elif userInput == "1":
                print("Start!")
                break
            elif userInput == "2":
                print("Help!")
                break
            elif userInput == "3":
                print("Exit!")
                break

    # Check if the user entered a correct letter
    def checkUserLetter(self, letter):
        letterCorrect = False

        # Loop through the chosen word, checking each letter
        for l in range(len(self.chosenWord)):
            # If the user guessed a letter correctly...
            if letter == self.chosenWord[l]:
                # Reveal its location in the game
                self.correctGuesses[l] = letter
                letterCorrect = True

        # If the user guessed a letter incorrectly, increment wrong guesses.
        if not letterCorrect:
            self.numWrongGuesses = self.numWrongGuesses + 1

    # Start game
    def playGame(self):

        # Setup new game
        self.setup()

        # Main game loop:
        while not (self.isGameOver()):

            # Show the Hangman picture
            subprocess.call(["cat", "./Drawings/hangman" + str(self.numWrongGuesses) + ".txt"])

            # Show user progress
            self.showProgress()

            # Get user input
            userInput = str(input("Enter a letter: "))

            # Check the input
            self.checkUserLetter(userInput)

        print("Game over!")
        
        if (self.numWrongGuesses == 6):
            subprocess.call(["cat", "./Drawings/gameover.txt"])
            print("You lose!")
            print("The word was: " + self.chosenWord)
        else:
            print("You win!")


    # Determine if the game is over
    def isGameOver(self):
        # Not exceeding the number of wrong guesses means game is not over
        # Any blank spaces also means the game is not over
        if (self.numWrongGuesses) < 6 and "_" in self.correctGuesses:
            return False

        return True

    def showHelp(self):
        pass

    # Show the progress of the user
    def showProgress(self):
        for i in range(len(self.correctGuesses)):
            print(self.correctGuesses[i], end=" ")
        print("\n")

if __name__ == "__main__":
    print("Running hangman tests...")

    hang1 = Hangman()

    # Test 1 & 2: Printing the menu and checking the input
    hang1.printMenu()
    # Test 3a: Testing the setup phase of the game.
#    hang1.setup() (WORKS)

    # Test 4: Gameplay
    hang1.playGame()
