# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
	# your code goes here
	if(type(x)==int):
		if x>0:
			if x%2==0:
				return True
			else: 
				return False
		else: 
			return False
	else: 
		return False
	

isevenpositiveint(9)
isevenpositiveint(-1)
isevenpositiveint(-2)
isevenpositiveint(-3)
isevenpositiveint(2)
isevenpositiveint(3)
isevenpositiveint(1.0)
isevenpositiveint("yikes!")
isevenpositiveint(None)
isevenpositiveint((12))
isevenpositiveint([12])
isevenpositiveint(123456)
