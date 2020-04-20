"""
https://cp-algorithms.com/algebra/euclid-algorithm.html
"""
def gcd_r(a, b):
    if b == 0:
        return a
    return gcd_r(b, a%b)

def gcd_i(a, b):
    if b == 0:
        return a

    while b:
        a %= b
        a, b = b, a

    return a

if __name__ == "__main__":
    from random import randint
    from time import time
    ITERS = 10000000

    """
    start = time()
    for i in range(ITERS):
        a, b = randint(1, 100), randint(1, 100)
        c = gcd_r(a, b)
    end = time()
    print("recursive: ", end-start)
    """
    
    start = time()
    for i in range(ITERS):
        a, b = randint(1, 100), randint(1, 100)
        c = gcd_i(a, b)
    end = time()
    print("iterative: ", end-start)
    
    import math

    start = time()
    for i in range(ITERS):
        a, b = randint(1, 100), randint(1, 100)
        c = math.gcd(a, b)
    end = time()
    print("Library: ", end-start)
