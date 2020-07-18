# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

def isprime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	else:
		return True

def fun_hasnoprimes(l):
	for i in l:
		for x in i:
			if isprime(x):
				# print(False)
				return False
	# print(True)
	return True
  


# fun_hasnoprimes([[9,12],[8],[16,8]])