### Get the greatest common divisor of 'a' and 'b'
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

### Extended euclidean algorithm
def gcde(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = gcde(b % a, a)
        return g, x - (b // a) * y, y

"""
Get the modular inverse of 'b' under modulus 'a'
I.e., returns x that b * x mod a = 1
"""
def modinv(a, b):
    g, x, y = gcde(b, a)
    return x % a

### Get cube root of 'x'
def root3(x):
    h = 1
    while h ** 3 <= x:
        h *= 2
    l = h // 2
    m = 0
    while l < h:
        m = (l + h) // 2
        if m ** 3 < x and l < m:
            l = m
        elif m ** 3 > x and h > m:
            h = m
        else:
            return m
    return m + 1

"""
Nx: the x-th modulus
Cx: the x-th encrypted message

return m: the plain text

Note: m*m*m should be smaller than N1 * N2 * N3
"""
def recover_msg(N1, N2, N3, C1, C2, C3):
    # Find t1 such that N2 * N3 * t1 % N1 = 1 where t1 is a positive integer
    t1 = modinv(N1, N2 * N3)

    # Find t2 such that N1 * N3 * t2 % N2 = 1 where t2 is a positive integer
    t2 = modinv(N2, N1 * N3)

    # Find t3 such that N1 * N2 * t3 % N3 = 1 where t3 is a positive integer
    t3 = modinv(N3, N1 * N2)

    # Then, m^3 can be found by:
    mCube = C1 * t1 * N2 * N3 + C2 * t2 * N1 * N3 + C3 * t3 * N1 * N2
    
    # Make sure that mCube is less than N1 * N2 * N3
    if mCube > N1 * N2 * N3:
        k = mCube // (N1 * N2 * N3)
        mCube = mCube - k * (N1 * N2 * N3)

    return root3(mCube)

def get_student_number():
    # TODO: Fill your student number here
    return "3035745037"
    
