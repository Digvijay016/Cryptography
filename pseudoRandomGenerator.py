# Python program to illustrate pseudo random generator
def seedLCG(initVal):
    global rand
    rand = initVal

def lcg():
    #a∈Z(Multiplicative group of prime) and b∈Z it
    #random number would be between a and c, also c and m are relatively prime
    multiplier = 1140671485
    increment = 128201163
    modulus = 2**31
    global rand
    # rand = (a*rand + c) % m
    rand = (multiplier * rand + increment) % modulus
    return rand

seedLCG(1)

print(lcg())
# for i in range(10):
#     print(lcg())


# # Python3 implementation of the
# # above approach
#
# # Function to generate random numbers
# def linearCongruentialMethod(Xo, m, a, c,randomNums,noOfRandomNums):
#     # Initialize the seed state
#     randomNums[0] = Xo
#
#     # Traverse to generate required
#     # numbers of random numbers
#     for i in range(1, noOfRandomNums):
#         # Follow the linear congruential method
#         randomNums[i] = ((randomNums[i - 1] * a) +
#                          c) % m
#
#
# # Driver Code
# if __name__ == '__main__':
#
#     # Seed value
#     Xo = 5
#
#     # Modulus parameter
#     m = 2**31
#
#     # Multiplier term
#     a = 1140671485#3
#
#     # Increment term
#     c = 128201163#3
#
#     # Number of Random numbers
#     # to be generated
#     noOfRandomNums = 10
#
#     # To store random numbers
#     randomNums = [0] * (noOfRandomNums)
#
#     # Function Call
#     linearCongruentialMethod(Xo, m, a, c,randomNums,noOfRandomNums)
#
#     # Print the generated random numbers
#     for i in randomNums:
#         print(i, end=" ")



# print("The formula is: X(k+1) = a * Xk + c mod m")
# seed_num = int(input("Enter seed number: "))
# multiplier = int(input("Enter the multiplier(a): "))
# increment = int(input("Enter the increment(c): "))
# modulus = int(input("Enter the modulus (m): "))
# unit = int(input("How many random numbers would you like to generate?\nInput: "))
#
#
# def lcg():
#     num_base = seed_num
#     for i in range(unit, 0, -1):
#         rd = (multiplier * num_base + increment) % modulus
#         print(rd)
#         num_base = rd
#
#
# lcg()