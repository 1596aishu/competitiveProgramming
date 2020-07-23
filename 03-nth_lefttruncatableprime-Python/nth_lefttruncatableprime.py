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
        c = -1
        n = str(n)
        x = n
        # print(x)
        while len(n)!=0:
            print(n)
            if isprime(int(n)):
                if "0" in n:
                    return False
                # print(n)
                n = n[1:]
                print(n)
                c+=1
            else:
                break
        if c == len(x):
            # print(True)
            return True
    # print(True)
    return False


def fun_nth_lefttruncatableprime(n):
    i = 0
    j = 2
    if n == 0:
        print(2)
        return 2
    while(i < n):
        if nthLeftTruncatablePrime(j):
            i += 1
        j += 1
    print(j-1)
    return j-1

fun_nth_lefttruncatableprime(1)