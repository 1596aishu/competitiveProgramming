# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2

def isprime(n):
	if n > 1:
		for i in range(2,n//2):
			if n % i ==0:
				return False
		else:
			return True


def fun_nth_additive_prime(n):
	c = 0
	i = 2
	while c!=n:		
		if isprime(i):
			sum=0
			temp = i
			while(temp != 0):
				x = temp % 10
				sum +=x
				temp = temp // 10
			if isprime(sum):
				c+=1
			i+=1
	return False		