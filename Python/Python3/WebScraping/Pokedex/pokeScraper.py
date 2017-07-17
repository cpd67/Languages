#!/bin/python3

# Web scraper that prints out the current National Pokedex

import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://pokemondb.net/pokedex/all")

soup = BeautifulSoup(webpage.content, 'html.parser')

# Get the National Pokedex numbers
pokeNums = list(soup.find_all(class_="num cell-icon-string"))
# Get the names of the Pokemon
pokeNames = list(soup.find_all(class_="ent-name"))
# Get their types
pokeTypes = list(soup.find_all(class_="cell-icon"))

for i in range(0, len(pokeNums)):
    # Print out the number and name
    print(pokeNums[i].get_text() + " " + pokeNames[i].get_text(), end=" ")

    # Check if we have two types
    types = list(pokeTypes[i].children)

    # If yes, print out the types with a space in-between them
    if (len(types) == 2):
        print(types[0].get_text(), end=" ")
        print(types[1].get_text())
        continue

    # Otherwise, just print out the one type
    print(types[0].get_text())
