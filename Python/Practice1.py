#!/bin/python

#Simple Python program, using basic control constructs
#and repetition constructs.
#List slicing = makes a new list

#The output looks nicer when using python3

#https://docs.python.org/3/tutorial/

#Like a #include...
import sys

#Arithmetic ops are the same as in other languages...

num = 1
num2 = 4
num3 = num + num2

print("(First print)")

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
print("(For loop with if-statement)")
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

	#To add...no switch statement exists in Python. 
	#The if-elif is a substitute. 
	#Makes sense. Usually a switch statement 
	#Requires the compiler to create a jump table.
	#Python's interpreted, so....

print("--------------------------------------")

print("(Modifying sequence inside of for loop)")

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
	print(n)

print("--------------------------------------")

print("(While loop)")

#While loop construct
count = 0
while count < 10:
	print("COUNTING IS FUN!")
	#No ++ operator :( Have to do this for incrementation
	count += 1

print("--------------------------------------")

print("(Multiple assignment)")

#Multiple assignment statements (which are COOL)
a,b = 4, 5

print("a is ", a)
print("b is ", b)
print("Swapping them...")

a,b = b,a

#Can print a number with a String using this syntax.
print("a is now ", a)
print("b is now ", b)

print("--------------------------------------")

print("(List slicing #1)")

#Examples of list slicing
lis1 = [2, 4, 6, 8, 1, 3, 5, 7]
lis2 = ['a', 'b', 'c', 'd', 'e']

#This splits lis1 and gets the first 4 numbers.
#One way to think of splitting:
# list[start:end] == end - start elements from list. 
lis3 = lis1[0:4]
for n in range(len(lis3)): #This syntax allows you to print both the index and element
	print(n, lis3[n])	   #of the list

print("--------------------------------------")

print("(List slicing #2)")

#Gives you the elements from 0 - 3
lis4 = lis1[:4]
for n in range(len(lis4)):
	print(n, lis4[n])

print("--------------------------------------")

print("(List slicing #3)")

#Gives you the elements from 1 - (length of lis1 - 1)
lis5 = lis1[1:]
for n in range(len(lis5)):
	print(n, lis5[n])

print("--------------------------------------")

print("(List slicing #4)")

#Gives you the whole list again
lis6 = lis1[:]
for n in range(len(lis6)):
	print(n, lis6[n])

print("--------------------------------------")
