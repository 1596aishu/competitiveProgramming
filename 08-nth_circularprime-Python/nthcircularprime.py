# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def nonzeroisprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i ==0:
				return False
		if "0" in str(n) or "2" in str(n) or "4" in str(n) or "6" in str(n) or "8" in str(n):
			return False
		return True


def circularprime(n):
	n = str(n)
	c = 1
	if len(n)==1:
		return True
	ls = n[1:]+n[:1]
	print(ls)
	while nonzeroisprime(int(ls)):
		ls = str(ls)		
		ls = ls[1:]+ls[:1]
		print(ls)
		c+=1
		print(c)
		if int(ls) == int(n):
			break
	if c == int(len(n))-1:
		return True
	return False

def nthcircularprime(n):
	# Your code goes here
	# pass
	i = 0
	j = 2
	while(i < n):
		if nonzeroisprime(j):
			if circularprime(j):
				i += 1
		j += 1
	print(j-1)
	return j-1
circularprime(3373)
# l = [(5, 13), (6, 17), (7, 31), (8, 37), 
# 	(9, 71), (10, 73), (11, 79), (12, 97), 
# 	(13, 113), (14, 131), (15, 197), (16, 199), 
# 	(17, 311), (18, 337), (19, 373), (20, 719), 
# 	(21, 733), (22, 919), (23, 971), (24, 991), 
# 	(25, 1193), (26, 1931), (27, 3119), (28, 3779), 
# 	(29, 7793), (30, 7937), (31, 9311), (32, 9377), 
# 	(33, 11939), (34, 19391), (35, 19937), (36, 37199), 
# 	(37, 39119), (38, 71993), (39, 91193), (40, 93719), 
# 	(41, 93911), (42, 99371), (43, 193939), (44, 199933), 
# 	(45, 319993), (46, 331999), (47, 391939)]
# m = []
# for i in range(len(l)):
# 	m.append((l[i][0]+1,l[i][1]))
# print(m)

