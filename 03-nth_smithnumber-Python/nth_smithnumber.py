# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22
def isprime(n):
	if n > 1:
		for i in range(2,n):
			if n % i ==0:
				return False
		return True

def smithnumber(n):
    p = n
    i = 2
    l = []
    while(n>1):
        if isprime(i):
            while(n%i == 0 and n >1):
                l.append(i)
                n //= i
        i += 1
    fac_sum = 0
    digit_sum = 0
    for i in l:
        fac_sum+=i
    for j in str(p):
        digit_sum+=int(j)
    if fac_sum == digit_sum:
        return True
    return False

def fun_nth_smithnumber(n):
    i = -1
    j = 2
    while(i < n):
        if isprime(j) != True:
            if smithnumber(j):
                # print(j)
                i += 1
        j += 1
    return j-1


# smithnumber(44)