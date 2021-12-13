# Python 3 program to find a prime factor of composite using
# Pollard's Rho algorithm
import random
import math
import Fast_Exp
import multiplicative_inverse

# Function to calculate (base^exponent)%modulus
def modular_pow(base, exponent ,modulus):

    # initialize result
    result = 1

    while (exponent > 0):

        # if y is odd, multiply base with result
        if (exponent & 1):
            result = (result * base) % modulus

        # exponent = exponent/2
        exponent = exponent >> 1

        # base = base * base
        base = (base * base) % modulus

    return result

# method to return prime divisor for n
def PollardRho(n):

    # no prime divisor for 1
    if (n == 1):
        return n

    # even number means one of the divisors is 2
    if (n % 2 == 0):
        return 2

    # we will pick from the range [2, N)
    x = (random.randint(0, 2) % (n - 2))
    y = x

    # the constant in f(x).
    # Algorithm can be re-run with a different c
    # if it throws failure for a composite.
    c = (random.randint(0, 1) % (n - 1))

    # Initialize candidate divisor (or result)
    d = 1

    # until the prime factor isn't obtained.
    # If n is prime, return n
    while (d == 1):

        # Tortoise Move: x(i+1) = f(x(i))
        x = (modular_pow(x, 2, n) + c + n ) %n

        # Hare Move: y(i+1) = f(f(y(i)))
        y = (modular_pow(y, 2, n) + c + n ) %n
        y = (modular_pow(y, 2, n) + c + n ) %n

        # check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)

        # retry if the algorithm fails to find prime factor
        # with chosen x and c
        if (d == n):
            return PollardRho(n)

    return d

def decrypt(enc_msg, n , k):
    # Bob will prime factorize n
    # n = p * q
    p = PollardRho(n)
    q = int(n / p)
    # print(p,q)
    phi_n = (p - 1) * (q - 1)
    # print(phi_n)
    inverse = multiplicative_inverse.modinv(k, phi_n)
    # print('Decryption Key', inverse)
    # print(inverse)
    # dr_msg = (en_msg ** inverse) % q
    # print(dr_msg)
    dr_msg = Fast_Exp.fast_exp(enc_msg, inverse, n)
    return dr_msg

# Driver function
if __name__ == "__main__":

    n = int(input('Enter n  : '))
    k = int(input('Enter k or e : '))
    en_msg = int(input('Enter Encrypted Message : '))

    # n = 15943
    n1 = PollardRho(n)
    n2 = n/n1
    print("One of the divisors for", n , "are " , n1, n2)

    # k = 3
    # en_msg = 5469
    #dmsg = 44

    dmsg = decrypt(en_msg, n, k)

    print("Decrypted Message :", dmsg);