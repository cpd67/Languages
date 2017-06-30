#!/bin/python3

# Guess The Number game
# ONLY WORKS WITH PYTHON3

import random

# Min and max range for the random number
MIN = 1
MAX = 7

# Store the random number
randNum = random.randrange(MIN, MAX)

print("Welcome to the \'Guess The Number\' game!")
print("The number will be between " + str(MIN) + " and " + str(MAX) + ".")

while True:
    # Convert the user inputted string into a number
    userGuess = int(input("Guess the number: "))
    if userGuess == randNum:
        print("You win!")
        break
    elif userGuess < randNum:
        print("Too low! Try again!")
    elif userGuess > randNum:
        print("Too high! Try again!")
