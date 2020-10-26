A, B, C, K = map(int, input().split())

res = 0

if K < A:
    print(K)

res += A
K -= A

if K:
    K -= B

if K > 0:
    res -= K

print(res)
