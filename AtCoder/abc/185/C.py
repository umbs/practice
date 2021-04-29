""" L choose R
"""
L = int(input())
cuts = 11

mem = [[0] * (cuts+1) for _ in range(L+1)]

# intialize
mem[3][1] = 1

for i in range(1, L+1):
    for j in range(1, cuts+1):
        if i == j + 1:
            mem[i][j] = 1

"""
Kinda combinatorics
mem[L][c] = Number of ways of cutting rod of length L using c cuts
mem[L][c] = mem[L-1][c-1]       # 1 inch cut and rest
            + mem[L-2][c-1]     # 2 inch cut and rest
            + mem[L-3][c-1]     # 3 inch cut and rest
            + mem[L-4][c-1]     # 4 inch cut and rest
"""

for i in range(2, L+1):
    for j in range(1, cuts+1):
        if j >= i:
            pass
        mem[i][j] = mem[i-1][j-1] + mem[i-2][j-1]

import pdb
pdb.set_trace()

print(mem[L][cuts])
