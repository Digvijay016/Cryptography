# Bob generates public and private keys:
    # Bob chooses a very large number q and a cyclic group Fq.
    # From the cyclic group Fq, he choose any element g and
    # an element a such that gcd(a, q) = 1.
    # Then he computes h = ga.
    # Bob publishes F, h = ga, q, and g as his public key and retains a as private key.

# Alice encrypts data using Bob’s public key :
    # Alice selects an element k from cyclic group F
    # such that gcd(k, q) = 1.
    # Then she computes p = gk and s = hk = gak.
    # She multiples s with M.
    # Then she sends (p, M*s) = (gk, M*s).
    # Bob decrypts the message :
    # Bob calculates s′ = pa = gak.
    # He divides M*s by s′ to obtain M as s = s′.
 
# Python program to illustrate ElGamal encryption

from math import pow,gcd as bltin_gcd,sqrt,ceil
import random

a = random.randint(2, 10)

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)

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

# Generating large random numbers
def gen_key(q):
    key = random.randint(pow(10, 2), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 2), q)

    return key

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


# Asymmetric encryption
def encrypt(msg, bh, g, x, q):
    # Alice public key (b,h,p)
    # b : Generator Of Group (g)
    # h : g^x (x = Alex Random Number)
    # p : q (modulus)
    # bh : Bob Public key

    en_msg = (msg * (bh**x)) % q
    return en_msg#, c1

def decrypt(en_msg, c1, y, q):
    # y is Bob Private Key
    # c1 is Alice Public key
    # q is modulus
    inv = c1**y
    inverse = modinv(inv,q)
    dr_msg = (inverse * en_msg) % q
    # print(dr_msg)
    return dr_msg

# Driver code
def main():
    msg = 114 #'data'
    print("Original Message :", msg)

    print('1 for Entire Simultaion of Bob and Alice')
    print('2 to fetch encrypted message and public key')
    print('3 to decrypt encrypted message')
    print('4 to generate Bob Public Key')

    inp = int(input('Enter your choice based on above : '))

    if inp == 1:

        primes = [i for i in range(1, 1000) if check_prime(i)]
        q = random.choice(primes)

        while msg > q:
            q = random.choice(primes)

        pri_roots = primRoots(q)
        g = random.choice(pri_roots)

        if g == 0:
            g = random.choice(pri_roots)

        x = random.randint(1,10)        # Alice Random Number Private Key
        ah = (g ** x)%q

        #bh = 378
        y = random.randint(1, 10)  # Bob Random Number Private Key
        bh = (g ** y) % q

        # q = 457
        # ah = 179
        # x = 5
        # bh = 32
        # y = 6
        # g = 184
        # en84
        # Decrypted
        # Message: 114

        en_msg = encrypt(msg, bh, g, x, q)
        print("q used : ",q)
        print("Alice h used : ",ah)
        print("Alice Private Key x used : ", x)
        print("Bob h used : ", bh)
        print("Bob Private Key y used : ", y)
        print("g used : ",g)
        print("Encrypted Message : ", en_msg)
        # print("Bob Public Key c1 used : ", c1)

        # print("Bob will post this public key (Enc Msg : {},Public Key : {})".format(en_msg, c1))
        dmsg = decrypt(en_msg, ah, y, q)

        print("Decrypted Message :", dmsg);

    if inp == 2:
        q = int(input('Enter prime q : '))
        g = int(input('Enter group generator g : '))
        bh = int(input('Enter Bob Public Key bh = g^x : '))
        x = int(input('Enter Alice Private Key x : '))
        # x = int

        # g = 2355
        # h = 2996
        # q = 12613

        print('q used : ', q)

        print("g used : ", g)
        # print("x used : ", x)
        print("bh = g^a used : ", bh)
        # print("Alice will post this public key (g : {},h = g^a : {},prime : {})".format(g,bh,q))

        en_msg = encrypt(msg, bh, g, x, q)
        print("Encrypted Message : ",en_msg)
        # print("Bob Public Key c1 used : ",c1)

        print("Alice will post this public key (Enc Msg : {} ,Bob Public Key : {})".format(en_msg, bh))

        # dmsg = decrypt(en_msg, c1,x, q)
        #
        # print("Decrypted Message :", dmsg);

    if inp == 3:

        q = int(input('Enter prime q : '))
        y = int(input('Enter Bob Private Key y : '))
        ah = int(input('Enter Alice public key ah : '))
        en_msg = int(input('Enter Encrypted Message : '))

        # q = 123
        # x = 11
        # c1 = 435
        # en_msg = 204


        dmsg = decrypt(en_msg, ah, y, q)

        print("Decrypted Message :", dmsg);

    if inp == 4:
        q = int(input('Enter prime q : '))
        g = int(input('Enter group generator g : '))
        # ah = int(input('Enter Alice public key ah : '))
        y = random.randint(1, 10)  # Bob Random Number Private Key
        bh = (g ** y) % q

        print("Bob Private key y : ",y)
        print("Bob Public Key : ", bh)


if __name__ == '__main__':
    main()