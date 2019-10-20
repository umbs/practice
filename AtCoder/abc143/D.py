from bisect import bisect_left as bl

N = int(raw_input())
L = list(map(int, raw_input().split()))
L = sorted(L)
print(L)

cnt = 0

for i in range(N):
    for j in range(i+1, N):
        idx = bl(L, L[i]+L[j])
        cnt += idx-j-1

print(cnt)
