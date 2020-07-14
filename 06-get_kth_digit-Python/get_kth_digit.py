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
		else:
			c = digit % 10
			print(c)
		i= i+1
	print(0)

fun_get_kth_digit(789,0)

