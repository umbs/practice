""" https://cp-algorithms.com/algebra/binary-exp.html
"""
def binpow(a, n):
    """ Recursive
    """
    if n == 0:
        return 1

    if n%2 == 0:
        res = binpow(a, n/2)
        return res * res

    else:
        res = binpow(a, (n-1)/2)
        return a * res * res


def binpow2(a, n):
    """ Iterative approach
    """
    res = 1
    while n:
        if n & 1:
            res = res * a
        a = a * a
        n >>= 1

    return res


if __name__ == "__main__":
    print(binpow2(2, 10))
