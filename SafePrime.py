# Python 3 implementation of the approach
from math import sqrt


# Function to print first n safe primes
def SafePrimes(n):
    prime = [0 for i in range(n + 1)]

    # Initialize all entries of integer
    # array as 1. A value in prime[i]
    # will finally be 0 if i is Not a
    # prime, else 1
    for i in range(2, n + 1):
        prime[i] = 1

    # 0 and 1 are not primes
    prime[0] = prime[1] = 0

    for p in range(2, int(sqrt(n)) + 1, 1):

        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == 1):

            # Update all multiples of p
            for i in range(p * 2, n + 1, p):
                prime[i] = 0

    for i in range(2, n + 1, 1):

        # If i is prime
        if (prime[i] != 0):

            # 2p + 1
            temp = (2 * i) + 1

            # If 2p + 1 is also a prime
            # then set prime[2p + 1] = 2
            if (temp <= n and prime[temp] != 0):
                prime[temp] = 2

    sf_prime_lst = []
    for i in range(5, n + 1):

        # i is a safe prime
        if (prime[i] == 2):
            sf_prime_lst.append(i)
            # print(i, end=" ")
    return  sf_prime_lst

# Driver code
if __name__ == '__main__':
    n = 100000
    # printSafePrimes(n)
    print(SafePrimes(n))