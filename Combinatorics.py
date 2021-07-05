""" L choose R
"""
L = int(input())
R = 12 

dp = [[0] * (R+1) for _ in range(L+1)]

for i in range(L+1):
    dp[i][0] = 1

for i in range(1, L+1):
    for j in range(i, R+1):
        if i == j:
            dp[i][j]  = 1

# Combinatorics: L choose 12
for i in range(1, L+1):
    for j in range(1, R+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[L][R])
