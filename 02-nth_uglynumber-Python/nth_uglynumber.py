# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def primefactors(n):
    l = []
    for i in range(2,n):
        if n%i == 0:
            if isprime(i):
                l.append(i)
    print(l)
    return l

def nthUglyNumber(n):
    return 0



def fun_nth_uglynumber(n):
    i = 0
    j = 2
    while i<n:
        if nthUglyNumber(j):
            i+=1
        j+=1
    print(n-1)
    return j-1

primefactors(2)