
import subprocess
import linecache
import random

class Hangman:

    # Class variables go here...

    def __init__(self):
        """ Constructor for the Hangman class. """

        # Instance variables...
        self.correct_guesses = []
        self.chosen_word = ""
        self.file_size_by_lines = 0
        self.num_wrong_guesses = 0

    def setup(self):
        """ Set up a new Hangman game. """

        subprocess.call(["clear"])

        rand_num = 0

        # https://stackoverflow.com/questions/19001402/how-to-count-the-total-number-of-lines-in-a-text-file-using-python
        # https://docs.python.org/3.3/tutorial/inputoutput.html
        # The 'with' keyword has the advantage that the file is properly closed after its suite is finished.
        with open('./words.txt', 'r') as file_handler:
            # Get the number of lines currently in the text file.
            self.file_size_by_lines = sum(1 for x in file_handler)

        rand_num = random.randrange(1, self.file_size_by_lines)

        # https://docs.python.org/3/library/linecache.html#module-linecache
        # Get random word from the text file.
        self.chosen_word = linecache.getline('./words.txt', rand_num)

        # Inspiration obtained from: https://stackoverflow.com/questions/18098326/dynamically-declare-create-lists-in-python
        # Use a list comp to create a list of blanks
        # based off the size of the chosen word.
        self.correct_guesses = ["_" for n in range((len(self.chosen_word)-1))]

    def print_menu(self):
        """ Show the menu for Hangman. """

        subprocess.call(["clear"])
        print("Welcome to Hangman!")
        print("Here are your options:")
        print("1. Play!")
        print("2. Help")
        print("3. Exit")

    def check_menu_input(self):
        """ Determine if player input at Hangman menu is valid. """

        while True:
            user_input = str(input("Enter your choice: "))
            if user_input not in ("1", "2", "3"):
                print("Invalid input!")
                self.print_menu()
            elif user_input == "1":
                self.play_game()
                break # FOR NOW
            elif user_input == "2":
                self.show_help()
                self.print_menu()
            elif user_input == "3":
                break

    def check_user_letter(self, letter):
        """ Determine if a guess entered by the player is correct. """

        letter_correct = False

        # Loop through the chosen word, checking each letter
        for index, l in enumerate(self.chosen_word):
            # If the user guessed a letter correctly...
            if letter == l:
                # Reveal its location in the game
                self.correct_guesses[index] = letter
                letter_correct = True

        # If the user guessed a letter incorrectly, increment wrong guesses.
        if not letter_correct:
            self.num_wrong_guesses = self.num_wrong_guesses + 1

        subprocess.call(["clear"])

    def play_game(self):
        """ Play Hangman! """

        # Setup new game
        self.setup()

        # Main game loop:
        while not (self.is_game_over()):

            # Show the Hangman picture
            subprocess.call(["cat", "./Drawings/hangman{}.txt".format(str(self.num_wrong_guesses))])

            # Show user progress
            self.show_progress()

            # Get user input
            user_input = str(input("Enter a letter: "))

            # Check the input
            self.check_user_letter(user_input)

        print("Game over!")

        if (self.num_wrong_guesses == 6):
            subprocess.call(["cat", "./Drawings/gameover.txt"])
            print("You lose!")
            print("The word was: {}".format(self.chosen_word))
        else:
            print("You win!")


    def is_game_over(self):
        """ Check if the game is complete. """

        # Not exceeding the number of wrong guesses means game is not over
        # Any blank spaces also means the game is not over
        if self.num_wrong_guesses < 6 and "_" in self.correct_guesses:
            return False

        return True

    def show_help(self):
        """ Display the help screen for Hangman. """

        subprocess.call(["clear"])
        with open("./help.txt", 'r') as file_handler:
            for line in file_handler:
                print(line)
        __ = input("Press any key to continue...")

    def show_progress(self):
        """ Show the number of letters the player has guessed correctly. """

        for i in range(len(self.correct_guesses)):
            print(self.correct_guesses[i], end=" ")
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
    hang1.print_menu()
    # Test 3a: Testing the setup phase of the game.
#    hang1.setup() (WORKS)

    # Test 4: Gameplay
    hang1.play_game()
