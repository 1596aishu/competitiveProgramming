# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	i = 0
	c = 0
	while digit!=0:
		if i!=k:
			digit= digit//10
		elif i==k:
			c = digit % 10
			print(c)
		else:
			print(0)
		i= i+1

fun_get_kth_digit(789,3)

