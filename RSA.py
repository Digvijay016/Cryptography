from math import pow,gcd as bltin_gcd,sqrt,ceil
import random

import Fast_Exp
import SafePrime

def egcd(a, b):                     #Extended Euc
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

def check_prime(num):
    for i in range(2,ceil(sqrt(num))):
        if num % i == 0:
            return False
    return True

# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c

def primRoots(modulo):
    if check_prime(modulo):
        required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo) }
        #print(required_set)
        return [g for g in range(1, modulo) if required_set == {power(g, powers, modulo)
                for powers in range(1, modulo)}]
    else:
        return "Number must be a prime number"


# Asymmetric encryption
def encrypt(msg, n, k):

    #Alice will send encrypted message to Bob with knowmn public keys (n,k)
    # enc_msg = (msg**k)%n
    enc_msg = Fast_Exp.fast_exp(msg, k, n)
    return enc_msg

def decrypt(en_msg, phi_n , n, k):
    print("Phi : ",phi_n)
    inverse = modinv(k,phi_n)
    print('Decryption Key : ', inverse)
    dr_msg = Fast_Exp.fast_exp(en_msg, inverse, n)
    return dr_msg

# Driver code
def main():
    msg = 44 #'data'
    print("Original Message :", msg)

############################################# Steps To Generate Alice Public Key ######################################

    print('1 for Entire Simultaion of Bob and Alice')
    print('2 to fetch encrypted message and public key')
    print('3 to decrypt encrypted message')

    inp = int(input('Enter your choice based on above : '))

    if inp == 1:
        # n = random.randint(pow(10, 5), pow(10,10)) # n can be any random number which can be split into two

        primes = SafePrime.SafePrimes(100000)
        a = random.choice(primes)
        b = random.choice(primes)

        if a == b:
            b = random.choice(primes)

        print("a used : ",a)
        print("b used :",b)
        n = a * b

        k = random.randint(100, 1000)

        # a = pollard_rho.PollardRho(n)
        # b = int(n / a)
        # print(a)
        # print(b)
        phi_n = (a-1)*(b-1)
        while(bltin_gcd(k,phi_n) != 1):
            # n = random.randint(pow(10, 5), pow(10, 10))  # n can be any random number which can be split into two

            k = random.randint(100, 1000)

        print("Alice will save this in her local machine (n : {} ,k : {}, a : {},b : {})".format(n, k, a, b))
        print("Alice will post this public key (n : {} ,k : {})".format(n, k))

        en_msg = encrypt(msg, n, k)
        print("Encrypted Message : ", en_msg)

        dmsg = decrypt(en_msg, phi_n, n, k)

        print("Decrypted Message :", dmsg);

    if inp == 2:
        n2 = int(input('Enter n  : '))
        k2 = int(input('Enter k : '))

        # n = 1392857819
        # k = 274308763

        print("Bob will post this public key (n : {} ,k : {})".format(n2,k2))

        en_msg = encrypt(msg, n2, k2)
        print("Encrypted Message : ",en_msg)

        # dmsg = decrypt(en_msg, n, k)
        #
        # print("Decrypted Message :", dmsg);

    if inp == 3:

        n = int(input('Enter n  : '))
        k = int(input('Enter k : '))
        a = int(input('Enter a  : '))
        b = int(input('Enter b  : '))

        phi_n = (a - 1) * (b - 1)
        en_msg = int(input('Enter Encrypted Message : '))

        # n = 617
        # k = 214
        # en_msg = 204

        # print("Alice will post this public key (n : {},k : {})".format(n,k))
        #
        # en_msg = encrypt(msg, n, k)
        # print("Encrypted Message : ",en_msg)

        dmsg = decrypt(en_msg, phi_n, n, k)

        print("Decrypted Message :", dmsg);

if __name__ == '__main__':
    main()