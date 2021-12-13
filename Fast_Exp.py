# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a Fast Exponential Algorithm script file.
"""

# #!/usr/bin/env python3
# def fast_exp(b, e, m):
#     r = 1
#     if 1 & e:
#         r = b
#     while e:
#         e >>= 1
#         b = (b * b) % m
#         if e & 1: r = (r * b) % m
#     return r

# def main():
#     b = int(input("Enter b:"))
#     e = int(input("Enter e:"))
#     m = int(input("Enter m:"))
#     r = fast_exp(b, e, m)
#     print("{} ^ {} ≡ {} (mod {})".format(b, e, r, m))

# if __name__ == '__main__':
#     main()

def fast_exp(b, e, m):
    r = 1
    print("X","\t\te","\t\tY")
    print("---------------------------------------------------------------------------------------------")
    print("{}\t\t{}\t\t{}".format(b, e, r))
    #if 1 & e:
    #    r = b
    while e:
        print("---------------------------------------------------------------------------------------------")
        #print("{}   {}   {}".format(b, e, r))
        if(e%2 == 0):
            e >>= 1
            b = (b * b) % m
            #if e & 1:     
            print("{}\t\t{}\t\t{}".format(b, e, r))
        else:
            e = e - 1
            r = (r * b) % m
            print("{}\t\t{}\t\t{}".format(b, e, r))
    print("---------------------------------------------------------------------------------------------")
    return r

def main():
    print("Computing b^e (mod m)")
    b = int(input("Enter b:"))
    e = int(input("Enter e:"))
    m = int(input("Enter m:"))
    r = fast_exp(b, e, m)
    print("Final Result : {} ^ {} (mod {}) ≡ {}".format(b, e, m, r))

if __name__ == '__main__':
    main()