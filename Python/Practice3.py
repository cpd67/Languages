#Python program for counting the number of times a letter appears in a string.

#Could return a tuple that gives you the index of the list
#and the value
#Also, learned that locals are NOT reassigned in for loop...
def findMax(lis):
	"""Finds the max element in a list."""
	index = [0]
	m1 = [-999999999]
	#Special use case: empty list
	if len(lis) == 0:
		return -1, -1
	#Special use case: list of size 1
	elif len(lis) == 1:
		return lis[0], 0
	#Normal case
	else:
		for n in range(len(lis)):
			if lis[n] > m1[0]:
				m1[0] = lis[n]
				index[0] = n
	#http://stackoverflow.com/questions/9752958/how-can-i-return-two-values-from-a-function-in-python
		return m1[0], index[0]

#index = 4, max = 1000
lis2 = [4, 8, 16, -1, 1000]

m1, in1 = findMax(lis2)

print("The max of lis2 is:", m1)
print("The index of " + str(m1) + " is " + str(in1))

#Special use case 1
lis3 = [10000000]

m2, in2 = findMax(lis3)

print("The max of lis3 is:", m2)
print("The index of " + str(m2) + " is " + str(in2))

#index = 0, max = 10
lis4 = [10, -1]
m3, in3 = findMax(lis4)

print("The max of lis4 is:", m3)
print("The index of " + str(m3) + " is " + str(in3))

#Utility function for finding index in a sequence
def findIndex(element, sequence):
	"""Finds the index of an element in a sequence."""
	for n in range(len(sequence)):
		if element == sequence[n]:
			return n
	return -1

def countReps(st1):
	"""Counts the number of repetitions a letter appears in a string sequence."""
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g' 'h' 'i','j','k','l', 'm','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v' 'w', 'x', 'y', 'z']
	counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for n in st1:
		index = findIndex(n, letters)
		counts[index] += 1
	mx, letterInd = findMax(counts)
	lett = letters[letterInd]
	print("The most frequent letter is " +  str(lett) + ", its count is " + str(mx))

#Test 1

st1 = "blaah"
countReps(st1)

st2 = "cowboy beep boop boop bop"
countReps(st2)
