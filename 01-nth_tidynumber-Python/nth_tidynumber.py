# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def nthTidyNumber(n):
    prev = 10
    while (n): 
        rem = n % 10
        n //= 10
        if rem > prev: 
            return False
        prev = rem 
    return True

def fun_nth_tidynumber(n):
    i = 0
    j = 2
    while i<n:
        if nthTidyNumber(j):
            i+=1
        j+=1
    print(j-1)
    return j-1

fun_nth_tidynumber(5)