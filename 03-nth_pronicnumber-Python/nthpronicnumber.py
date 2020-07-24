# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronicnumber(n):
	sum = n*(n+1)
	return sum

def nthpronicnumber(n):
	# Your code goes here
	i = 1
	j = 1
	sum1 = 0
	if n == 0:
		return 0
	while i < n:
		sum1 = pronicnumber(j)
		i+=1
		j+=1
	print(sum1)
	return sum1

nthpronicnumber(2)