N = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(N):
    x = A[l]
    for r in range(l, N):
        x = min(x, A[r])
        ans = max(ans, (r-l+1) * x)

print(ans)
