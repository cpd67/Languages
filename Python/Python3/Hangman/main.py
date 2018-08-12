# Need to use the 'from' clause when dealing with classes
from hangman import *

if __name__ == "__main__":

	game = Hangman()
	game.print_menu()
	game.check_menu_input()
