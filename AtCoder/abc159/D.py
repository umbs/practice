""" Solution belongs to: https://atcoder.jp/contests/abc159/submissions/11124930
"""
N = int(raw_input())
A = map(int, raw_input().split())
 
count = [0]*(N+1)
for i in range(N):
    id = A[i]
    count[id] = count[id]+1
 
sumN = long(0)
for i in range(N+1):
    sumN = sumN + long(long(count[i]*(count[i]-1))/2)
 
for i in range(N):
    id = A[i]
    sumz = sumN - (count[id] - 1)
    print(sumz)
