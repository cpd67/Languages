#!/bin/python

#Looking at more functions, and much more!

print("-----------------------------------------")

print("(Pass example)")

#The pass keyword is used as a placeholder when you don't
#have the body of the function made yet...
def countUpTo(n):
	pass

#Every function returns something in Python, surprisingly.
#Even those that don't return something explicitly.
#Those that do so return 'None'.

print(countUpTo(5))

print("-----------------------------------------")
print("(Renaming functions)")

#Since user-defined functions have a type in Python,
#You can assign them to variables and call them through the variables.
#Wow.

newFun = countUpTo

print(newFun(4))

print("-----------------------------------------")
print("(Default parameters and the \'in\' keyword)")

print
print

#Wow, just, wow.
#I already knew about default parameters, which are formal parameters that are 
#assigned a value by default (so long as no actual parameter is passed).
#But what I didn't know about, was the 'in' keyword used in conjunction with 
#an if-statement.
#It essentially tests if something is within a sequence.
#THIS CODE ONLY WORKS WITH PYTHON3!!
def fun(prompt, tries=3, reminder='NEIN!'):
	while True:
		p = input(prompt)
		if p in ('y', 'yes', 'YES'):
			print("You asked for it.")
			return True
		if p in ('n', 'no', 'nope', 'NO', 'NOPE'):
			print("Really? Alright. Your call.")
			return False
		tries = tries - 1
		if tries <= 0:
			print("No more tries! Bye!")
			return False
		print(reminder)

fun('Would you like to quit?', 3, 'Say \'yes\' or \'no\'')


print("-----------------------------------------")
