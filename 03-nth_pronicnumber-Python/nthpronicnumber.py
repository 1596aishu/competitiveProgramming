# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def pronicnumber(n):
	sum = n*n+1
	

def nthpronicnumber(n):
	# Your code goes here
	i = 0
	j = 2
	while i < n:
		sum = pronicnumber(j)
		i+=1
		j+=1
	print(sum)
	return sum