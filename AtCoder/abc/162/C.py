import math

K = int(input())
trip = dict()
pair = dict()

def gcd(a, b):
    d = frozenset([a, b])
    if d in pair:
        return pair[d]

    if b == 0:
        pair[d] = a
        return a

    while b:
        a %= b
        a, b = b, a

    pair[d] = a
    return a

def gcd3(K):

    res = 0

    for i in range(1, K+1):
        for j in range(1, K+1):
            for k in range(1, K+1):
                l = frozenset([i, j, k])
                if l in trip:
                    res += trip[l]
                    continue

                x = gcd(i, gcd(j, k))
                # print("i:%d, j:%d, k:%d, x:%d" % (i, j, k, x))
                res += x
                trip[l] = x

    return res

def sol(K):
    res = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            t = math.gcd(i, j)
            for k in range(1, K+1):
                res += math.gcd(k, t)

    return res
print(sol(K))
