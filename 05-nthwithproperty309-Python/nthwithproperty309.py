# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.
def property309(c):
	n = c**5
	# print(c,n)
	lst = [0,1,2,3,4,5,6,7,8,9]
	for i in str(n):
		for j in lst:
			if int(i) == j:
				lst.remove(j)
	# print(lst)
	if len(lst)>=1:
		return False
	return True

def nthwithproperty309(n):
	# Your code goes here
	# pass
	i = 1
	c = 310
	while i!=n:
		# print("x")
		if property309(c):
			# print("true")
			i+=1
		c+=1
	print(c)
	return c
		
nthwithproperty309(2)
