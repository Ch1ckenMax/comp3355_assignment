"""
N: the modulus

return (p, q): the factors of N
"""
def get_factors(N):

    if N % 2 == 0:
        return 2, N // 2

    # From now on, we only need to check odd numbers
    potentialPrimeFactor = 3
    primeFactorizationFound = False

    while (not primeFactorizationFound) and potentialPrimeFactor <= N**(1/2): 
        # Check if potentialPrimeFactor is a prime number
        if not isPrime(potentialPrimeFactor):
            potentialPrimeFactor = potentialPrimeFactor + 2
            continue
        
        # Check if the modulus is divisible by the potentialPrimeFactor
        if N % potentialPrimeFactor != 0:
            potentialPrimeFactor = potentialPrimeFactor + 2
            continue

        # Given the assumption that N is a product of two prime numbers, and N has a unique prime factorization 
        # Once we found a prime p such that N is divisible by p, p and q = N // potentialPrimeFactor is the prime factorization of N
        primeFactorizationFound = True

    return potentialPrimeFactor, (N // potentialPrimeFactor)

"""
p, q: the factors of N
e: the encryption exponent

return d: the decryption exponent
"""
def get_private_key_from_p_q_e(p, q, e):
    phi = (p - 1) * (q - 1)
    d = modinv(phi, e)
    return d

def get_student_number():
    # TODO: Fill your student number here
    return "3035745037"
    
# Given an integer, determine whether it is a prime number
def isPrime(number: int) -> bool:
    if number % 2 == 0:
        return False

    # We only need to check odd numbers from now on
    potentialFactor = 3
    while potentialFactor <= number**(1/2):
        if number % potentialFactor == 0:
            return False
        potentialFactor = potentialFactor + 2
    return True