#!/bin/python

#Practice Python program #2

#Continuation of repetition constructs
#and control structures..
#Functions...


#Let's play!
lis1 = [1, 2, 3, 4, 6, 8, 9, 12]

print("-------------------------------")
print("(Continue example)")

#continue statement goes to the next iteration of the loop.
#This is also in C.
#Perfect for not having an extra else check
#should an if-statement be in a for loop.
#(Efficiency!) 
for n in lis1:
	if n % 2 == 0:
		print("Even number")
		print("Next iteration, please!")
		continue
	print("Odd number")

print("-------------------------------")
print("Function example #1")


