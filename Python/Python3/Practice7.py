#!/bin/python3

# List comprehensions, classes, and objects

# Listcomps usually consist of brackets containing an expression by a for
# clauses, then 0 or more if clauses.
# The result is a new list from evaluating the expression in the context
# of the for and if clauses that follow it.
print("---------------------------------")
print("List comprehensions")

squares = [x**2 for x in range(10)]
print(squares)
