# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:56:42 2021

@author: Digvijay Singh

Assignment 

Problem Prime Factorization
"""
from math import ceil, sqrt

def check_prime(num):
    for i in range(2,ceil(sqrt(num))):
        if num % i == 0:
            return False
    return True

def prime_fac(num):
    a = num
    pf = []
    for x in range(2,a):
        if a % x == 0:
            if x == 2 or x == 3:
                pf.append(x)
                a = a//x
            else:
                for y in range(2,x):
                    if (x % y) == 0:
                        break
                else:
                    pf.append(x)
                    a = a // x
        else:
            continue
    if a>1:
        pf.append(a)
    print (f"Prime factors of {num} are {pf}")
    return pf

number = int(input('Enter a number to find its prime factors: '))
res = prime_fac(number)

print(check_prime(res[0]))
print(check_prime(res[1]))