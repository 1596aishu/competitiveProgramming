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
	l1 = []
	for i in range(2,n):
		while n%i == 0:
			if isprime(i):
				l.append(i)
			i+=1
	for i in l:
		if n&(i**2) == 0:
			l1.append(i)
	if len(l) == len(l1):
		return True
	return False

def nthpowerfulnumber(n):
	# Your code goes here
	# pass
	if n == 0:
		return 1
	c = 0
	i = 2
	while c!=n:
		if powerfulNumber(i):
			c+=1
		if c == n:
			return i
		i+=1


		
	
	

nthpowerfulnumber(4)


