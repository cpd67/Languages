#!/bin/python
# Dice Rolling Simulator
# THIS CODE ONLY WORKS WITH PYTHON3

import random

MIN = 1
MAX = 7

def rollDice():
    print("Let's roll some dice!")
    print("Rolling...")
    print("The dice roll is: " + str(random.randrange(MIN, MAX)))

rollDice()

while True:
    x = input('Would you like to roll again? ')
    if x in ("y", "Y", "yes", "YES", "ye"):
        print ("Okay!")
        rollDice()
        continue
    elif x in ("n", "N", "no", "NO"):
        print ("Fine. Partypooper.")
        break
    print ("I didn't understand that. Please try again.")
