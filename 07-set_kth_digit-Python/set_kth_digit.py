# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	i = 0
	num = n
	while n!=0:
		if i==k:
			p = n%10
			# print(p)
			N = str(num)
			N=N.replace(str(p),str(d),1)
			# print(N)
			print(int(N))
		elif i!=k:
			n= n//10
			
		i= i+1
fun_set_kth_digit(468, 0, 1)

