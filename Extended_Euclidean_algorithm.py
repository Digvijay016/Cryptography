# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 15:29:31 2021

@author: Digvijay Singh

Assignment 

Problem Extended Euclidean Algorithm
"""

"""
    gcd(30, 50) = 10
    Here, x = 2 and y = -1 since 30*2 + 50*-1 = 10
     
    gcd(2740, 1760) = 20
    Here, x = 9 and y = -14 since 2740*9 + 1760*-14 = 20
"""

# Python program for the extended Euclidean algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x
 
 
if __name__ == '__main__':
 
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    gcd, x, y = egcd(a, b)
    print("The GCD of {} and {} is {}".format(a,b,gcd))
    print(f"x = {x}, y = {y}")
