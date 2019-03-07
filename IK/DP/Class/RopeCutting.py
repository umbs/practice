''' 
Given a rope of length L and an array of price points (for varying
lengths), how to cut the rope to maximize earnings 

Ex:
length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

- Let S[j] = Max price for rope of length L
- Then S[k] for k > j is:
    max of S[j] + price[k-j] for all j from 1 to k-1
'''

def ropeCut(L, price):
    ''' price has cost of every length between 0 and L'''
    S = [0] * (L+1)
    for i in range(1, L+1):
        opt = -1
        for j in range(i):
            opt = max(opt, S[j] + price[j-i])
        S[i] = opt

    return S[L]

def ropeCutBruteForce(L, price):
    if not L:
        return 0

    opt = 0
    for i in range(1, L+1):
        opt = max(opt, price[i] + ropeCutBruteForce(L-i, price)
    return opt
