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

def fib(n):
	"""This is a docstring."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
	print()

#Call the puppy we just defined.
fib(100000)

#Also learning about symbol tables.
#Apparently, variable assignments in a function store the value in a local one.
#Variable references look in the local, then local of enclosing functions, then in 
#global, and lastly the table of built-in names. 
#Also, Python has call-by-value parameter passing.
print("-------------------------------")

#Function example 2
#Didn't need to look this up ;-)
def maxLis(lis1):
	"""Gets the maximum from a sequence of numbers"""
	m1 = -999999
	for n in lis1:
		if n > m1:
			m1 = n
	return m1

#Test
lis = [4, 8, 100, 0]
m2 = maxLis(lis)

print("Lis values: ")

for n in lis:
	print(n, end=",")

print()
print("The max of lis is: ", m2)		


