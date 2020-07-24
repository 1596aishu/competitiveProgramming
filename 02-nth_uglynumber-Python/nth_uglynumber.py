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
    if n<10:
        if isprime(n):
            l.append(n)
        else:
            for i in range(2,n):
                if n%i == 0:
                    if isprime(i):
                        l.append(i)

    else:
        for i in range(2,n):
            if n%i == 0:
                if isprime(i):
                    l.append(i)
    print(n,l)
    return l

def nthUglyNumber(n):
    lst = []
    lst = primefactors(n)
    c = 0
    l = [2,3,5]
    for i in l:
        if i in lst:
            c +=1
    if c!=0:
        return True
    return False



def fun_nth_uglynumber(n):
    i = 0
    j = 2
    while i<n:
        if nthUglyNumber(j):
            i+=1
        j+=1
    print(j-1)
    return j-1

fun_nth_uglynumber(10)