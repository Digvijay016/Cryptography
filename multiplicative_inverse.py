# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:20:46 2021

@author: Digvijay Singh

Assignment 

Problem Multiplicative Inverse
"""

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        #print("{}\t\t{}\t\t{}".format(g,y,x))
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    #print("{}\t\t{}\t\t{}".format(g,y,x))
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

a = 3
b = 11
# print('EGCD : ',egcd(2,3))
print("Modular inverse of ({}*x) mod {} = 1, x = {}".format(a,b,modinv(a,b)))
# Input:  a = 3, m = 11
# Output: 4
# Since (4*3) mod 11 = 1, 4 is modulo inverse of 3(under 11).
# One might think, 15 also as a valid output as "(15*3) mod 11" 
# is also 1, but 15 is not in ring {1, 2, ... 10}, so not 
# valid.