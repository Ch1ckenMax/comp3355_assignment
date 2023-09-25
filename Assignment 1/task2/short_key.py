"""
N: the modulus

return (p, q): the factors of N
"""
def get_factors(N):

    if N % 2 == 0:
        return 2, N // 2

    # From now on, we only need to check odd numbers (any prime number that is larger than 2 is odd)
    potentialPrimeFactor = 3
    primeFactorizationFound = False
    upperBound = N**(1/2) # Just in case to prevent infinite loop

    while (not primeFactorizationFound) and potentialPrimeFactor <= upperBound: 
        # Check if the modulus is divisible by the potentialPrimeFactor
        # Given the assumption that N is a product of two prime numbers, and N has a unique prime factorization. If we found a potentialPrimeFactor such that N % potentialPrimeFactor:
        #   If potentialPrimeFactor is a prime number, then we found the answer.
        #   If potentialPrimeFactor is not a prime number:
        #       We can further do prime factorization to potentialPrimeFactor
        #       Then, N has a prime factorization that is a product of more than two numbers
        #       Our assumption states that N has a prime factorization of product of two numbers. Which is a contradiction
        # Hence, potentialPrimeFactor must be a prime number
        if N % potentialPrimeFactor != 0:
            potentialPrimeFactor = potentialPrimeFactor + 2
        else:
            primeFactorizationFound = True

    return potentialPrimeFactor, (N // potentialPrimeFactor)

"""
p, q: the factors of N
e: the encryption exponent

return d: the decryption exponent
"""
def get_private_key_from_p_q_e(p, q, e):
    phi = (p - 1) * (q - 1)
    k = 0

    while True:
        term = k * phi + 1
        d = term // e

        # Check if d satisfies the two conditions
        if (k * phi + 1) % e == 0 and d != e:
            return d
        
        # Try the next k
        k = k + 1

def get_student_number():
    # TODO: Fill your student number here
    return "3035745037"