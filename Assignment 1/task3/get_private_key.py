### Get the greatest common divisor of 'a' and 'b'
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

"""
N1: your modulus
N2: your classmate's modulus

return result: True if n1 and n2 share the same prime number; otherwise, returns False
"""
def is_waldo(n1, n2):
    result = False

    divisor = gcd(n1, n2)

    # Given the assumption that n1 and n2 are both product of two prime numbers
    # There is no way that their gcd is not a prime number and not equal to 1, otherwise, n1 and n2 has more than 1 prime factorization, which is a contradiction
    # Hence, the divisor is either a prime number or 1 (n1 and n2 are co-prime => no prime number divides n1 and n2)
    return divisor != 1

"""
This function will be called if is_waldo(n1, n2) returns True.

N1: your modulus
N2: your classmate's modulus
e: the encryption exponent

return d: the decryption exponent
"""
def get_private_key_from_n1_n2_e(n1, n2, e):
    d = 0
    
    commonPrime = gcd(n1, n2)
    anotherPrime = n1 // commonPrime

    # Get d from commonPrime and anotherPrime
    phi = (commonPrime - 1) * (anotherPrime - 1)
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
    
