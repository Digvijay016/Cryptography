# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:53:02 2021

@author: Digvijay Singh

Assignment 4

Problem 2
Baby-Step Giant-Step Algorithm
"""


# from math import ceil, sqrt


# def bsgs(g, h, p):
#     '''
#     Solve for x in h = g^x mod p given a prime p.
#     e.g. 2^x equivalent to 7 mod 53 solve for x.
#     If p is not prime, you shouldn't use BSGS anyway.
#     '''
#     N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

#     # Store hashmap of g^{1...m} (mod p). Baby step.
#     tbl = {pow(g, i, p): i for i in range(N)}

#     # Precompute via Fermat's Little Theorem
#     c = pow(g, N * (p - 2), p)

#     # Search for an equivalence in the table. Giant step.
#     for j in range(N):
#         y = (h * pow(c, j, p)) % p
#         if y in tbl:
#             return j * N + tbl[y]

#     # Solution not found
#     return None


# print(bsgs(3, 2, 29))

from math import ceil, sqrt

def baby_step_giant_step(y, a, n):
    #Baby Step Giant Step DLP problem y = a**x mod n or loga(y) in Zn 
    #Example 70 = 2**x mod 131 my programme will give output of x
    s = int(ceil(sqrt(n)))
    A = [y * pow(a, r, n) % n for r in range(s)]
    B = [pow(a,t*s,n) % n for t in range(1,s+1)]
    # A.sort()
    # B.sort()
    print("List A is: ",A)
    print("List B is: ",B)
    for r in A:
        for t in B:
            if r == t:
                x1 = A.index(r)            
                x2 = B.index(t)
                break
    print("Collision occurs from List A at x1 =",x1,"and from List B at x2 =",x2)
    for t in range(1,s+1):
        value = pow(a, t*s, n)
        #print(value)
        if value in A:
            return (t * s - A.index(value)) % n

y = int(input("Enter value of y : "))
a = int(input("Enter value of a : "))
n = int(input("Enter value of n : "))

print("\nThe value of x is ",baby_step_giant_step(y,a,n))
print("\nNow you can try Fast exponential algorithm to test your output")