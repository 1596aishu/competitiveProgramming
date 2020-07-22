# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i ==0:
				return False
		return True


def circularprime(n):
	n = str(n)
	if len(n)==1:
		return True
	ls = n[1:]+n[:1]
	# print(ls)
	rs = n[len(n)-1:]+n[:len(n)-1]
	# print(rs)
	rs = int(rs)
	ls = int(ls)
	if isprime(ls) and isprime(rs):
		return True
	return False

def nthcircularprime(n):
	# Your code goes here
	# pass
	c = 1
	i = 2
	if "0" in str(i):
		return None
	else:
		while c!=n:
			# print(c)
			if isprime(i):
				if circularprime(i):
					# print("circular prime:"+i)
					c+=1
			i+=1
		return i


nthcircularprime(7)