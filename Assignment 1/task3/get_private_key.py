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
    # TODO: Implement this function for Task 3
    return result

"""
This function will be called if is_waldo(n1, n2) returns True.

N1: your modulus
N2: your classmate's modulus
e: the encryption exponent

return d: the decryption exponent
"""
def get_private_key_from_n1_n2_e(n1, n2, e):
    d = 0
    # TODO: Implement this function for Task 3
    return d

def get_student_number():
    # TODO: Fill your student number here
    return ""
    
