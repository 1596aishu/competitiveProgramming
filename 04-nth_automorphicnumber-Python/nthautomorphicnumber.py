# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.


def automorphic(n):
	sq = n**2
	x=int(str(sq)[-(len(str(n))):])
	if n == x:
		return True
	return False

def nthautomorphicnumbers(n):
	# Your code goes here
	# pass
	i = 2
	j = 2
	while i<n:
		if automorphic(j):
			i+=1
		j+=1
	print(j-1)
	return j-1

nthautomorphicnumbers(5)