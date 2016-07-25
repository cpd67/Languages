#!/bin/python

#Simple Python program, using basic control constructs
#and repetition constructs.

#Like a #include...
import sys

#Arithmetic ops are the same as in other languages...

num = 1
num2 = 4
num3 = num + num2

print(num3)

num4 = num - num2
num5 = num * num2
num6 = num / num2
num7 = num // num2 #Floor division; truncates the mantissa of a float.

#List sequence
nums = [num3, num4, num5, num6, num7]

#For loop construct
#Similar to a for-each loop in Java 5
for n in nums:
	#If-statement construct
	#No implicit type casting; have to do explicit type casting
	#an exception is with numeric types; e.g. int to float
	#str(#) typecasts an int into a str
	if n > 0:
		print(str(n) + " is greater than 0")
	elif n < 0:
		print(str(n) + " is less than 0")
	elif n == 0:
		print("ZERO")
	else:
		print("No idea...")

#While loop construct
count = 0
while count < 10:
	print("COUNTING IS FUN!")
	#No ++ operator :( Have to do this for incrementation
	count += 1

