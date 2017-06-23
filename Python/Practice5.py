#!/bin/python
# Dice Rolling Simulator
# THIS CODE ONLY WORKS WITH PYTHON3

import random

MIN = 1
MAX = 7

def getRandomNumber():
    return random.randrange(MIN, MAX)

print ("Let's roll some dice!")
print ("Rolling...")
print ("The dice roll is: " + str(getRandomNumber()))

while True:
    x = input('Would you like to roll again? ')
    if x in ("y", "yes", "YES", "ye"):
        print ("Okay! Let's roll again!")
        print ("Rolling...")
        print ("The dice roll is: " + str(getRandomNumber()))
        continue
    elif x in ("n", "no", "NO"):
        print ("Fine. Partypooper.")
        break
    print ("I didn't understand that. Please try again.")
