#!/bin/python

#Simple Python program, using basic control constructs
#and repetition constructs.
#https://docs.python.org/3/tutorial/

#Like a #include...
import sys

#Arithmetic ops are the same as in other languages...

num = 1
num2 = 4
num3 = num + num2

print(num3)

print("--------------------------------------")

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

print("--------------------------------------")

#Modifying the sequence inside of the for loop
# = Make a slice copy of the list to iterate over,
#Then, modify the original inside of the loop.
#Smart. It prevents you from modifying the original 
#while also looping through it, because that could be BAD.
for n in nums[:]:
	if n > 4:
		#Insert the number at position 0 in the list
		nums.insert(0, n)

#Print out the new number list
for n in nums:
	print(str(n))

print("--------------------------------------")

#While loop construct
count = 0
while count < 10:
	print("COUNTING IS FUN!")
	#No ++ operator :( Have to do this for incrementation
	count += 1

print("--------------------------------------")

#Multiple assignment statements (which are COOL)
a,b = 4, 5

print("a is "+ str(a))
print("b is " + str(b))
print("Swapping them...")

a,b = b,a

print("a is now " + str(a))
print("b is now " + str(b))

print("--------------------------------------")

