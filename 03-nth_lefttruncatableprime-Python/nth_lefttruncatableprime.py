# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retuns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def isprime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def nthLeftTruncatablePrime(n):
    if n<10:
        if isprime(n):
            return n
    else:
        c = 1
        n = str(n)
        while len(n)!=0:
            if isprime(int(n)):
                c+=1
                n = n[1:]
            if c == len(n)-1:
                print(c)


def fun_nth_lefttruncatableprime(n):
    i = 0
    j = 2
    while i<n:
        if nthLeftTruncatablePrime(i):
            return True
    return 1

nthLeftTruncatablePrime(317)