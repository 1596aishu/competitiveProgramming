# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math
def isperfectsquare(n):
	# your code goes here
	if type(n)==int and n>0:
		if type(math.sqrt(n)) == int:
			print(True)
			return True
		else: 
			print(False)
			return False
	else:
		if type(n) == str and n>0:
			try:
				m = int(n)
				if type(math.sqrt(m)) == int and m>0:
					print(True)
					return True
				else:
					print(False)
					return False
			except:
				print(False)
				return False
		else:
			print(False)
			return False

isperfectsquare(4)
isperfectsquare(-625)


