# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	# pass
	lst = []
	for i in L:
		for j in i:
			if j not in lst:
				lst.append(j)
			elif j in lst:
				return True
	return False
