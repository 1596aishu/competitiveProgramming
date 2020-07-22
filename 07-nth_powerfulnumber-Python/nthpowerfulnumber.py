# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math
def isprime(n):
	for i in range(2,n):
		if n%i == 0:
			return False
	return True

def primeFactors(Number):
	# no of even divisibility
	i = 1
	while(i <= Number):
		count = 0
		if(Number % i == 0):
			j = 1
			while(j <= i):
				if(i % j == 0):
					count = count + 1
				j = j + 1
				
			if (count == 2):
				print(" %d is a Prime Factor of a Given Number %d" %(i, Number))
		i = i + 1
	
	

def powerfulNumber(n):
	l = []
	l1 = []
	for i in l:
		if n%(i**2) == 0:
			l1.append(i)
	# print(l)
	if len(l) == len(l1):
		print(True)
		return True
	print(False)
	return False

def nthpowerfulnumber(n):
	# Your code goes here
	# pass
	if n == 0:
		print(1)
		return 1
	i = 0
	j = 2
	while(i < n):
		if powerfulNumber(j):
			i += 1
		j += 1
	print(j)
	return j	
	
	

primeFactors(36)


