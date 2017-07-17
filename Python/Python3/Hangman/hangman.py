

# TODO: Make game code more efficient...

import subprocess
import linecache
import random

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

        subprocess.call(["clear"])

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
        subprocess.call(["clear"])
        print("Welcome to Hangman!")
        print("Here are your options:")
        print("1. Play!")
        print("2. Help")
        print("3. Exit")

    # Determine if user input at menu is valid
    def checkMenuInput(self):
        while True:
            userInput = str(input("Enter your choice: "))
            if userInput not in ("1", "2", "3"):
                print("Invalid input!")
                self.printMenu()
            elif userInput == "1":
                self.playGame()
                break # FOR NOW
            elif userInput == "2":
                self.showHelp()
                self.printMenu()
            elif userInput == "3":
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

        subprocess.call(["clear"])

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
        subprocess.call(["clear"])
        with open("./help.txt", 'r') as fileHandler:
            for line in fileHandler:
                print(line)
        __ = input("Press any key to continue...")

    # Show the progress of the user
    def showProgress(self):
        for i in range(len(self.correctGuesses)):
            print(self.correctGuesses[i], end=" ")
        print("\n")

# When you run a Python module with the python command, the code will be executed
# but with the __name__ variable set to "__main__".
# Essentially, the code after the if statement will be executed only if this file
# is being executed as a script.
# You can also just import this module in another module using import.
if __name__ == "__main__":
    print("Running hangman tests...")

    hang1 = Hangman()

    # Test 1 & 2: Printing the menu and checking the input
    hang1.printMenu()
    # Test 3a: Testing the setup phase of the game.
#    hang1.setup() (WORKS)

    # Test 4: Gameplay
    hang1.playGame()
