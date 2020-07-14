# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math
def isperfectsquare(n):
	# your code goes here
	if type(n)==int and n>0:
		# if type(math.sqrt(n)) == int:
		a = int(math.sqrt(n))
		if math.sqrt(n) == a:
			print("True1")
			return True
		else: 
			print("False2")
			return False
	else:
		if type(n) == str:
			try:
				m = int(n)
				b = int(math.sqrt(m))
				if math.sqrt(m) == b and m>0:
					print("True2")
					return True
				else:
					print("False2")
					return False
			except:
				print("False3")
				return False
		else:
			print("False4")
			return False

isperfectsquare("hello")
isperfectsquare("100")
isperfectsquare(6.25)
isperfectsquare(100)


