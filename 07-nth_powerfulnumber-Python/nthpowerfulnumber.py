# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def isprime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

def powerfulNumber(n):
	l = []
	for i in range(2,n):
		while n%i == 0:
			if isprime(i):
				l.append(i)
			i+=1
	print(set(l))
	return l

def nthpowerfulnumber(n):
	# Your code goes here
	# pass
	return powerfulNumber(n)
	

nthpowerfulnumber(36)


