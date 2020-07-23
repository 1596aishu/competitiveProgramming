# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def nthKaprekarNumber(n):
    sq = n**2
    sq = str(sq)
    sq1 = sq[:(len(sq)//2)]
    sq2 = sq[(len(sq)//2):]
    # print(sq1,sq2)
    sum = 0
    sum = int(int(sq1)+int(sq2))
    print(type(sum))
    if sum == n:
        return True
    return True

def fun_nth_kaprekarnumber(n):
    i = 0
    j =  2
    if n == 0:
        return 1
    while(i<n):
        if nthKaprekarNumber(j):
            i += 1
        j += 1
    return j-1
nthKaprekarNumber(703)