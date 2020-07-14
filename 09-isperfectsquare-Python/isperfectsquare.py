# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
	# your code goes here
	if type(n)==int:
		if type(math.sqrt(n)) == int:
			return True
		else: 
			return False
	else:
		if type(n) == str:
			try:
				n = int(n)
				if type(math.sqrt(n)) == int:
					return True
				else:
					return False
			except:
				return False
		else:
			return False


