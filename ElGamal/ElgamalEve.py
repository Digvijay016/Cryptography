import math

from sympy.polys.domains import ZZ

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

# p : Prime Modulus
# b : Group Generator
# h : Alice Public Key
# c1 : Bob Public Key
# enc_msg

# q = 495433
# h = 482693
# g = 5
# c1 = 41828
# c2 = 330193

# q = 131                   # group G
# g = 2                     # Primitive Root
# x = 5                     # random number selected by alice
# h = g**x                  # h:=g^{order of group}
# y = 7                     # random number selected by Bob
# c1 = g**y                 # c1 = g^y -- y is a random integer from 1 to q - 1
# c2 = 87*((h)**y)        # c2 = m.s --[s = h^y], m = message if number else convert the string to message
# c2 = 2989297238016      # E(x)


# p = int(input('Enter prime q : '))
# b = int(input('Enter generator g or b : '))
# h = int(input('Enter h = g^x : '))
# c1 = int(input('Enter public key c1 : '))
# enc_msg = int(input('Enter Encrypted Message : '))

# p = 29023
# b = 3
# h = 6487                #b^r
# c1 = 28160               #b^l
# enc_msg = 457534        #enc_msg

# p = 823
# b = 3
# h = 353                #b^r
# c1 = 328               #b^l
# enc_msg = 634        #enc_msg

p = 29023
b = 3
h = 6487                #b^r
c1 = 18571               #b^l
enc_msg = 593340        #enc_msg

p = 151
b = 6
h = 117                #b^r
c1 = 126               #b^l
enc_msg = 1776        #enc_msg


p = 1019
b = 2
h = 302                #b^r
c1 = 380               #b^l
enc_msg = 797        #enc_msg
#dec msg = 111

# p = 827
# b = 785
# h = 357                #b^r
# c1 = 599               #b^l
# enc_msg = 351        #enc_msg
#dec msg = 114

p = 1823
b = 143
h = 363                #b^r
c1 = 724               #b^l
enc_msg = 156954        #enc_msg

q = p
g = b
h = h
c1 = c1
c2 = enc_msg

m = math.sqrt(q - 1)
m = int(math.ceil(m))

# print(m)
# m = 113

def findxwithBSGS(g, q, h, m):
    values = dict()

    for j in range(m):
        baby = pow(g,j,q)
        values[baby] = j

    y = pow(g, m * (q - 2), q)

    for i in range(m):
        giant = (h * pow(y, i, q) % q)

        try:
            return i * m + values[giant]
        except:
            pass

x = findxwithBSGS(g, q, h, m)
# print(x)
def findMsg(q, x, c1, c2):
    s = pow(c1, x, q)
    inv = modinv(ZZ(s),ZZ(q))
    msg = ZZ((inv * c2) % q)
    return msg

msg = findMsg(q, x, c1, c2)

print("Secret Message using BSGS is: "+str(msg))